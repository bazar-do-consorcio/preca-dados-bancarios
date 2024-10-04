import json
import logging
import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv

# Criação do logger e definição do nível de log
logger = logging.getLogger()
logger.setLevel(logging.INFO)

if not logger.hasHandlers():
    # Configuração do manipulador para saída no terminal
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)

load_dotenv()

URL_PIPEFY = os.getenv('URL_PIPEFY')
PIPEFY_TOKEN = os.getenv('PIPEFY_TOKEN')
id_webhook = None

def lambda_handler(event, context):
    try:
        resultado = processar_webhook_resposta(event['body'])
        
        return resultado
    except Exception as e:
        logger.error("Erro interno no servidor: %s", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps("Erro interno no servidor. Verifique os logs para mais detalhes.", ensure_ascii=False)
        }
    
def processar_webhook_resposta(body):

    global id_webhook

    resposta = json.loads(body)
    validacao_data = resposta['data']

    id_webhook = resposta['data']['id']
    logger.info(f"ID do webhook capturado: {id_webhook}")

    if validacao_data.get('valid') is True:
        return processar_sucesso(validacao_data)
    else:
        return processar_erro(validacao_data)
    

def processar_sucesso(validacao_data):
    dados_validos = 'VALIDO'

    # Obter a URL pré-assinada
    url_pre_assinada = obter_url_pre_assinada("301247725", "comprovante_microdeposito.pdf")
    logger.info(f"URL pré-assinada obtida: {url_pre_assinada}")

    # Extrair o caminho formatado da URL
    caminho_formatado = extrair_caminho(url_pre_assinada)
    logger.info(f"Caminho formatado: {caminho_formatado}")

    # Fazer o upload do arquivo
    arquivo_url = validacao_data.get('receipt_url')
    logger.info(f"Validacao data: {validacao_data}")
    logger.info(f"Receipt URL: {arquivo_url}")

    sucesso_upload = fazer_upload(url_pre_assinada, arquivo_url)
    if sucesso_upload:
        logger.info("Upload realizado com sucesso.")

        # Atualizar campos no Pipefy
        resposta_atualizacao = atualizar_campos_pipefy(
            node_id="971537587",
            dados_validos=dados_validos,
            erro_dados_bancarios="",
            caminho_arquivo=caminho_formatado  # Adiciona o caminho do comprovante
        )
        logger.info(f"Resposta da atualização: {resposta_atualizacao}")

        # Verifique se o comprovante precisa ser atualizado
        if dados_validos and caminho_formatado:
            atualizar_comprovante(node_id="971537587", caminho_arquivo=caminho_formatado)

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

def processar_erro(validacao_data):
    erros = validacao_data.get('errors', [])
    erros_formatados = formatar_erros(erros)

    # Atualizar campos no Pipefy com erro
    atualizar_campos_pipefy(
        node_id="971537587",
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
    url = 'https://api.pipefy.com/graphql'
    headers = {
        "Authorization": f"Bearer {PIPEFY_TOKEN}",
        "Content-Type": "application/json"
    }
    query = f"""
    mutation {{
        createPresignedUrl(input: {{ organizationId: {id_organizacao}, fileName: "{nome_arquivo}" }}) {{
            url
        }}
    }}
    """
    response = requests.post(url, headers=headers, json={'query': query})
    return response.json()['data']['createPresignedUrl']['url']


def fazer_upload(url_pre_assinada, arquivo):
    headers = {
        'Content-Type': 'application/pdf'
    }
    response = requests.put(url_pre_assinada, headers=headers, data=requests.get(arquivo).content)

    if response.status_code == 200:
        logger.info("Upload realizado com sucesso.")
    else:
        logger.error(f"Falha no upload. Status Code: {response.status_code}, Resposta: {response.text}")

    return response.status_code == 200


def extrair_caminho(url_pre_assinada):
    parsed_url = urlparse(url_pre_assinada)
    caminho = parsed_url.path.lstrip('/')

    # Adicionando "orgs/" ao caminho
    partes = caminho.split('/')
    if len(partes) >= 5:
        return "/".join(partes[0:2]) + "/" + "/".join(partes[2:])  # Inclui "orgs/" e o restante
    return caminho  # Se não tiver partes suficientes, retorna o caminho completo


def atualizar_campos_pipefy(node_id, dados_validos, erro_dados_bancarios=None, caminho_arquivo=None):
    url = 'https://api.pipefy.com/graphql'
    headers = {
        "Authorization": f"Bearer {PIPEFY_TOKEN}",
        "Content-Type": "application/json"
    }

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

    logger.info("Enviando mutação para o Pipefy: %s", variables)

    response = requests.post(url, json={'query': mutation, 'variables': variables}, headers=headers)

    if response.status_code == 200:
        logger.info("Campos atualizados com sucesso: %s", response.json())

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
            response_comprovante = requests.post(url, headers=headers, json={'query': mutation_comprovante})
            logger.info("Comprovante atualizado: %s", response_comprovante.json())
            return response_comprovante.json()

    else:
        logger.error("Erro ao atualizar os campos: %s - %s", response.status_code, response.text)
    return response.json()


def atualizar_comprovante(node_id, caminho_arquivo):
    url = 'https://api.pipefy.com/graphql'
    headers = {
        "Authorization": f"Bearer {PIPEFY_TOKEN}",
        "Content-Type": "application/json"
    }
    mutation = f"""
    mutation {{
        updateCardField(input: {{ card_id: {node_id}, field_id: "comprovante_microdeposito", new_value: ["{caminho_arquivo}"] }}) {{
            clientMutationId
            success
        }}
    }}
    """
    response = requests.post(url, headers=headers, json={'query': mutation})
    logger.info("Comprovante atualizado: %s", response.json())
    return response.json()


if __name__ == "__main__":

    node_id  = 971537587
    dados_bancarios = {
        # "version": "v1",
        # "id": "053d4115-464c-45eb-b026-a7040690fa9a",
        # "account_id": "e22ca638-4d5f-4310-85c0-3eb370e82345",
        # "object": "Validation",
        # "date": "2024-09-30T09:37:32-03:00",
        # "data": {
        #     "id": "125c310d-f208-47ef-a235-9524f08a5c4e", #pegar esse id na resposta
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
        #         "field": "cpf_cnpj",
        #         "message": "CPF 35271737598 inválido",
        #         "errorCode": "DBA_28"
        #     },
        #     {
        #         "field": "account_digit",
        #         "message": "Agência, conta ou dígito verificador da conta inválido.",
        #         "errorCode": "DBA_30",
        #         "suggestion": {
        #         "account_digit": "5"
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
        "id": "379dcb53-8484-49af-b542-a59918608a76",
        "account_id": "e22ca638-4d5f-4310-85c0-3eb370e82345",
        "object": "Validation",
        "date": "2024-09-30T15:02:39-03:00",
        "data": {
            "id": "a685c577-0a46-4388-be2c-5db1ad824f05",
            "integration_id": None,
            "created_at": "2024-09-30T18:02:36.000Z",
            "pre_validated_at": None,
            "validated_at": None,
            "bank_code": "237",
            "bank_ispb": None,
            "micro_deposit_status": "VALIDADO",
            "micro_deposit_value": None,
            "micro_deposit_method": "PIX",
            "valid": True,
            "errors": [],
            "receipt_url": "https://api-sandbox.transfeera.com/pub/receipt/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFuc2Zlcl9pZCI6IjE0NTcwMzMiLCJyZWNlaXB0X3R5cGUiOiJ0cmFuc2ZlZXJhIiwiYmF0Y2hfdHlwZSI6IlRSQU5TRkVSRU5DSUEiLCJpYXQiOjE3Mjc3MTkzNTksImV4cCI6MTczMjkwMzM1OX0.sdgChnHOdEApu_36NsScrhAIU3ExoyBqc-KZLffjuEY",
            "bank_receipt_url": "https://api-sandbox.transfeera.com/pub/receipt/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFuc2Zlcl9pZCI6IjE0NTcwMzMiLCJyZWNlaXB0X3R5cGUiOiJiYW5rIiwiYmF0Y2hfdHlwZSI6IlRSQU5TRkVSRU5DSUEiLCJpYXQiOjE3Mjc3MTkzNTksImV4cCI6MTczMjkwMzM1OX0.f_Muw3VCHbXsggXomQrKyLK_x6woj_LqGd8aU2aHibo",
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
    logger.info("Resultado da execução do lambda_handler: %s", result)



