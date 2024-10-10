import json
import logging
import requests
import os

from urllib.parse import urlparse
from dotenv import load_dotenv
from micro_deposito import obter_cabecalhos

logger = logging.getLogger()
logger.setLevel(logging.INFO)

if not logger.hasHandlers():
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)

load_dotenv()

URL_PIPEFY = os.getenv('URL_PIPEFY')
PIPEFY_TOKEN = os.getenv('PIPEFY_TOKEN')

def lambda_handler(event, context):
    try:
        resultado = processar_webhook_resposta(event['body'])
        return resultado
    except Exception as e:
        logger.error("Erro interno: %s", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps("Erro interno no servidor. Verifique os logs para mais detalhes.", ensure_ascii=False)
        }
    

def consultar_card_no_pipefy(transfeera_id):
    query = f"""
    {{
        findCards(pipeId: 303852432
                  search: {{fieldId: "transfeera_id", fieldValue: "{transfeera_id}"}}
                  first: 10) {{
            nodes {{
                id
                fields {{
                    name
                    value
                }}
            }}
        }}
    }}"""

    response = requests.post(URL_PIPEFY, headers=obter_cabecalhos(), json={"query": query})

    if response.status_code == 200:
        nodes = response.json().get("data", {}).get("findCards", {}).get("nodes", [])
        if nodes:
            return nodes[0]
        logger.info(f"Card com transfeera_id {transfeera_id} não encontrado no Pipefy.")
    else:
        logger.error("Erro ao buscar card no Pipefy: %d %s", response.status_code, response.text)
    return None

    
def processar_webhook_resposta(body):
    resposta = json.loads(body)
    validacao_data = resposta['data']

    # Obtém o transfeera_id do webhook
    transfeera_id = validacao_data.get('id')

    if transfeera_id:
        # Buscar o card com o transfeera_id
        card = consultar_card_no_pipefy(transfeera_id)
        
        if card:

            node_id = card['id']

            if validacao_data.get('valid') is True:
                return processar_sucesso(validacao_data, node_id)
            else:
                return processar_erro(validacao_data, node_id)
    else:
            return {
                'statusCode': 404,
                'body': json.dumps(f"Card com transfeera_id {transfeera_id} não encontrado no Pipefy.")
            }

    
def processar_sucesso(validacao_data, node_id):
    dados_validos = 'VALIDO'

    # Obter a URL pré-assinada, ID da organização
    url_pre_assinada = obter_url_pre_assinada("301247725", "comprovante_microdeposito.pdf")
    logger.info(f"URL pré-assinada obtida: {url_pre_assinada}")

    # Extrair o caminho formatado da URL
    caminho_formatado = extrair_caminho(url_pre_assinada)
    logger.info(f"Caminho formatado: {caminho_formatado}")

    # Fazer o upload do arquivo
    arquivo_url = validacao_data.get('receipt_url')
    logger.info(f"Validacao data: {validacao_data}")

    sucesso_upload = fazer_upload(url_pre_assinada, arquivo_url)
    if sucesso_upload:
        atualizar_campos_pipefy(
            node_id=node_id,
            dados_validos=dados_validos,
            erro_dados_bancarios="",
            caminho_arquivo=caminho_formatado 
        )

        # Verifique se o comprovante precisa ser atualizado
        if dados_validos and caminho_formatado:
            atualizar_comprovante(node_id=node_id, caminho_arquivo=caminho_formatado)

    else:
        logger.error("Falha ao realizar o upload do arquivo.")

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Conta validada com sucesso',
            'account_info': {
                'agencia': validacao_data.get('agency', 'AGENCIA_DESCONHECIDA'),
                'conta': validacao_data.get('account', 'CONTA_DESCONHECIDA'),
                'cpf_cnpj': validacao_data.get('cpf_cnpj', 'CPF_CNPJ_DESCONHECIDO'),
                'tipo_conta': validacao_data.get('account_type', 'TIPO_CONTA_DESCONHECIDA'),
                'digito_conta': validacao_data.get('account_digit', 'DIGITO_DESCONHECIDO'),
                "receipt_url": validacao_data.get('receipt_url', 'URL_DESCONHECIDA')
            },
        }, ensure_ascii=False)
    }

def processar_erro(validacao_data, node_id):
    erros = validacao_data.get('errors', [])
    erros_formatados = formatar_erros(erros)
    logger.info(f"Validacao data: {validacao_data}")

    atualizar_campos_pipefy(
        node_id=node_id,
        dados_validos="INVALIDO",
        erro_dados_bancarios=erros_formatados
    )

    return {
        'statusCode': 400,
        'body': json.dumps({
            'message': 'Dados inválidos',
            'errors': erros_formatados
        }, ensure_ascii=False)
    }


def formatar_erros(erros):
    mapa_campos = {
        "name": "Nome",
        "cpf_cnpj": "CPF_CNPJ",
        "bank_code": "Código do Banco",
        "agency": "Agência",
        "account": "Conta",
        "account_digit": "Dígito da Conta",
        "account_type": "Tipo de Conta"
    }

    mensagens_formatadas = []

    for erro in erros:
        campo = erro['field']
        mensagem = erro['message']

        campo_formatado = mapa_campos.get(campo, campo)
        mensagens_formatadas.append(f'{campo_formatado}: {mensagem}')

    return '. '.join(mensagens_formatadas)


def obter_url_pre_assinada(id_organizacao, nome_arquivo):
    query = f"""
    mutation {{
        createPresignedUrl(input: {{ organizationId: {id_organizacao}, fileName: "{nome_arquivo}" }}) {{
            url
        }}
    }}
    """
    response = requests.post(URL_PIPEFY, headers=obter_cabecalhos(), json={'query': query})
    return response.json()['data']['createPresignedUrl']['url']


def fazer_upload(url_pre_assinada, arquivo):
    response = requests.put(url_pre_assinada, headers={'Content-Type': 'application/pdf'}, data=requests.get(arquivo).content)

    if response.status_code == 200:
        logger.info("Upload realizado com sucesso.")
    else:
        logger.error(f"Falha no upload. Status Code: {response.status_code}, Resposta: {response.text}")

    return response.ok


def extrair_caminho(url_pre_assinada):
    parsed_url = urlparse(url_pre_assinada)
    caminho = parsed_url.path.lstrip('/')

    # Adicionando "orgs/" ao caminho
    partes = caminho.split('/')
    if len(partes) >= 5:
        return "/".join(partes[0:2]) + "/" + "/".join(partes[2:])  # Inclui "orgs/" e o restante
    return caminho  # Se não tiver partes suficientes, retorna o caminho completo


def atualizar_campos_pipefy(node_id, dados_validos, erro_dados_bancarios=None, caminho_arquivo=None):
    mutation = """
    mutation ($nodeId: ID!, $values: [NodeFieldValueInput!]!) {
        updateFieldsValues(input: {
            nodeId: $nodeId,
            values: $values
        }) {
            clientMutationId
        }
    }
    """
    values = [{'fieldId': "dados_v_lidos", 'value': dados_validos}]  # Use a variável diretamente

    if erro_dados_bancarios is not None:
        values.append({'fieldId': "erro_dados_bancarios", 'value': erro_dados_bancarios})

    variables = {
        'nodeId': node_id,
        'values': values
    }

    response = requests.post(URL_PIPEFY, headers=obter_cabecalhos(), json={'query': mutation, 'variables': variables})

    if response.status_code == 200:
        # Atualiza o campo de comprovante se necessário
        if dados_validos and caminho_arquivo:
            mutation_comprovante = f"""
            mutation {{
                updateCardField(input: {{ card_id: {node_id}, field_id: "comprovante_microdeposito", new_value: ["{caminho_arquivo}"] }}) {{
                    clientMutationId
                    success
                }}
            }}
            """
            response_comprovante = requests.post(URL_PIPEFY, headers=obter_cabecalhos(), json={'query': mutation_comprovante})
            return response_comprovante.json()

    else:
        logger.error("Erro ao atualizar os campos: %s - %s", response.status_code, response.text)
    return response.json()


def atualizar_comprovante(node_id, caminho_arquivo):

    mutation = f"""
    mutation {{
        updateCardField(input: {{ card_id: {node_id}, field_id: "comprovante_microdeposito", new_value: ["{caminho_arquivo}"] }}) {{
            clientMutationId
            success
        }}
    }}
    """
    response = requests.post(URL_PIPEFY, headers=obter_cabecalhos(), json={'query': mutation})
    return response.json()


if __name__ == "__main__":
    dados_bancarios = {
        # "version": "v1",
        # "id": "6a75b919-2716-4d8f-a8a3-bc6bd7b3a22f",
        # "account_id": "e22ca638-4d5f-4310-85c0-3eb370e82345",
        # "object": "Validation",
        # "date": "2024-10-07T10:26:05-03:00",
        # "data": {
        #     "id": "ea793454-9f0e-4ff6-8d6b-12813c4d64db",
        #     "integration_id": None,
        #     "pre_validated_at": None,
        #     "validated_at": None,
        #     "bank_code": None,
        #     "bank_ispb": None,
        #     "micro_deposit_status": None,
        #     "micro_deposit_value": None,
        #     "micro_deposit_method": None,
        #     "valid": False,
        #     "errors": [
        #     {
        #         "field": "account_digit",
        #         "message": "Conta ou dígito verificador da conta inválido.",
        #         "errorCode": "DBA_20",
        #         "suggestion": {
        #         "account_digit": "6"
        #         }
        #     }
        #     ],
        #     "receipt_url": None,
        #     "bank_receipt_url": None,
        #     "pix_description": None,
        #     "source": "API",
        #     "data": None,
        #     "person_type": None,
        #     "person_type_details": None
        # }
        "version": "v1",
        "id": "3f66df44-b6a0-45f8-b1a5-4e1b3f60a5bb",
        "account_id": "e22ca638-4d5f-4310-85c0-3eb370e82345",
        "object": "Validation",
        "date": "2024-10-08T11:36:02-03:00",
        "data": {
            "id": "ea793454-9f0e-4ff6-8d6b-12813c4d64db",
            "integration_id": None,
            "created_at": "2024-10-08T14:35:57.000Z",
            "pre_validated_at": None,
            "validated_at": None,
            "bank_code": "237",
            "bank_ispb": None,
            "micro_deposit_status": "VALIDADO",
            "micro_deposit_value": None,
            "micro_deposit_method": "PIX",
            "valid": True,
            "errors": [],
            "receipt_url": "https://api-sandbox.transfeera.com/pub/receipt/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFuc2Zlcl9pZCI6IjE0NjQ0MTYiLCJyZWNlaXB0X3R5cGUiOiJ0cmFuc2ZlZXJhIiwiYmF0Y2hfdHlwZSI6IlRSQU5TRkVSRU5DSUEiLCJpYXQiOjE3MjgzOTgxNjIsImV4cCI6MTczMzU4MjE2Mn0.EU1CUSt_avnk4kZqv_cau1tHF6c8a1LauC9DIpkrDEg",
            "bank_receipt_url": "https://api-sandbox.transfeera.com/pub/receipt/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFuc2Zlcl9pZCI6IjE0NjQ0MTYiLCJyZWNlaXB0X3R5cGUiOiJiYW5rIiwiYmF0Y2hfdHlwZSI6IlRSQU5TRkVSRU5DSUEiLCJpYXQiOjE3MjgzOTgxNjIsImV4cCI6MTczMzU4MjE2Mn0.gghbKV5o50ulSyJxwGHuE_GMMpeS-hC-IElVvC6un9g",
            "pix_description": None,
            "source": "API",
            "data": {
            "name": "Transfeera Pagamentos",
            "agency": "2232",
            "account": "40605",
            "cpf_cnpj": "27084098000169",
            "bank_code": "237",
            "account_type": "CONTA_CORRENTE",
            "account_digit": "8"
            },
            "person_type": "legal_entity",
            "person_type_details": None
        }
    }

    dados_clientes_json = json.dumps(dados_bancarios, ensure_ascii=False, indent=4)

    event = {
        "body": dados_clientes_json
    }
    context = None

    result = lambda_handler(event, context)



