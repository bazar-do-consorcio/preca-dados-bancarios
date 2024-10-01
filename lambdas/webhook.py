import json
import logging
import requests
import os
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
    resposta = json.loads(body)

    # Cenário de Sucesso
    validacao_data = resposta['data']

    if validacao_data.get('valid') is True:
        dados_validos = 'VALIDO',
        comprovante_url = validacao_data.get('receipt_url', 'URL_COMPROVANTE_DESCONHECIDA')

        # Atualizar campos no Pipefy
        atualizar_campos_pipefy(
            node_id="971537587",
            dados_validos=dados_validos
        )

        # Anexar o comprovante PDF ao campo "comprovante_microdep_sito"
        anexar_comprovante_pipefy("971537587", comprovante_url)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Conta validada com sucesso',
                'account_info': {
                    'agencia': validacao_data['data'].get('agency', 'AGENCIA_DESCONHECIDA'),
                    'conta': validacao_data['data'].get('account', 'CONTA_DESCONHECIDA'),
                    'cpf_cnpj': validacao_data['data'].get('cpf_cnpj', 'CPF_CNPJ_DESCONHECIDO'),
                    'tipo_conta': validacao_data['data'].get('account_type', 'TIPO_CONTA_DESCONHECIDA'),
                    'digito_conta': validacao_data['data'].get('account_digit', 'DIGITO_DESCONHECIDO')
                },
            }, ensure_ascii=False)
        }
    
    else:
        # Cenário de erro
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


def anexar_comprovante_pipefy(card_id, attachment_url):
    mutation = """
    mutation ($card_id: ID!, $field_id: String!, $attachment_url: String!) {
      updateCardField(input: {
        card_id: $card_id,
        field_id: $field_id,
        new_value: [$attachment_url]
      }) {
        clientMutationId
        success
      }
    }
    """
    variables = {
        "card_id": card_id,
        "field_id": "comprovante_microdep_sito",
        "attachment_url": attachment_url
    }

    data = {
        'query': mutation,
        'variables': variables
    }

    headers = {
        "Authorization": f"Bearer {PIPEFY_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(URL_PIPEFY, json=data, headers=headers)

    if response.status_code == 200:
        logger.info("Comprovante anexado com sucesso: %s", response.json())
    else:
        logger.error("Erro ao anexar comprovante: %s - %s", response.status_code, response.text)




def atualizar_campos_pipefy(node_id, dados_validos, erro_dados_bancarios=None):
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

    values = [
        {'fieldId': "dados_v_lidos", 'value': dados_validos},
    ]

    if erro_dados_bancarios is not None:
        values.append({'fieldId': "erro_dados_bancarios", 'value': erro_dados_bancarios})

    variables = {
        'nodeId': node_id,
        'values': values
    }

    data = {'query': mutation, 'variables': variables}
    headers = {
        "Authorization": f"Bearer {PIPEFY_TOKEN}",
        "Content-Type": "application/json"
    }

    logger.info("Enviando mutação para o Pipefy: %s", data)

    response = requests.post(URL_PIPEFY, json=data, headers=headers)

    if response.status_code == 200:
        logger.info("Campos atualizados com sucesso: %s", response.json())
    else:
        logger.error("Erro ao atualizar os campos: %s - %s", response.status_code, response.text)


if __name__ == "__main__":

    node_id  = 971537587
    dados_bancarios = {
        "version": "v1",
        "id": "053d4115-464c-45eb-b026-a7040690fa9a",
        "account_id": "e22ca638-4d5f-4310-85c0-3eb370e82345",
        "object": "Validation",
        "date": "2024-09-30T09:37:32-03:00",
        "data": {
            "id": "125c310d-f208-47ef-a235-9524f08a5c4e",
            "integration_id": None,
            "pre_validated_at": None,
            "validated_at": None,
            "bank_code": None,
            "bank_ispb": None,
            "micro_deposit_status": None,
            "micro_deposit_value": None,
            "micro_deposit_method": None,
            "valid": False,
            "errors": [
            {
                "field": "cpf_cnpj",
                "message": "CPF 35271737598 inválido",
                "errorCode": "DBA_28"
            },
            {
                "field": "account_digit",
                "message": "Agência, conta ou dígito verificador da conta inválido.",
                "errorCode": "DBA_30",
                "suggestion": {
                "account_digit": "5"
                }
            }
            ],
            "receipt_url": None,
            "bank_receipt_url": None,
            "pix_description": None,
            "source": "API",
            "data": None,
            "person_type": None,
            "person_type_details": None
        }
        # "version": "v1",
        # "id": "379dcb53-8484-49af-b542-a59918608a76",
        # "account_id": "e22ca638-4d5f-4310-85c0-3eb370e82345",
        # "object": "Validation",
        # "date": "2024-09-30T15:02:39-03:00",
        # "data": {
        #     "id": "a685c577-0a46-4388-be2c-5db1ad824f05",
        #     "integration_id": None,
        #     "created_at": "2024-09-30T18:02:36.000Z",
        #     "pre_validated_at": None,
        #     "validated_at": None,
        #     "bank_code": "237",
        #     "bank_ispb": None,
        #     "micro_deposit_status": "VALIDADO",
        #     "micro_deposit_value": None,
        #     "micro_deposit_method": "PIX",
        #     "valid": True,
        #     "errors": [],
        #     "receipt_url": "https://api-sandbox.transfeera.com/pub/receipt/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFuc2Zlcl9pZCI6IjE0NTcwMzMiLCJyZWNlaXB0X3R5cGUiOiJ0cmFuc2ZlZXJhIiwiYmF0Y2hfdHlwZSI6IlRSQU5TRkVSRU5DSUEiLCJpYXQiOjE3Mjc3MTkzNTksImV4cCI6MTczMjkwMzM1OX0.sdgChnHOdEApu_36NsScrhAIU3ExoyBqc-KZLffjuEY",
        #     "bank_receipt_url": "https://api-sandbox.transfeera.com/pub/receipt/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFuc2Zlcl9pZCI6IjE0NTcwMzMiLCJyZWNlaXB0X3R5cGUiOiJiYW5rIiwiYmF0Y2hfdHlwZSI6IlRSQU5TRkVSRU5DSUEiLCJpYXQiOjE3Mjc3MTkzNTksImV4cCI6MTczMjkwMzM1OX0.f_Muw3VCHbXsggXomQrKyLK_x6woj_LqGd8aU2aHibo",
        #     "pix_description": None,
        #     "source": "API",
        #     "data": {
        #     "name": "Transfeera Pagamentos",
        #     "agency": "2232",
        #     "account": "40605",
        #     "cpf_cnpj": "27084098000169",
        #     "bank_code": "237",
        #     "account_type": "CONTA_CORRENTE",
        #     "account_digit": "8"
        #     },
        #     "person_type": "legal_entity",
        #     "person_type_details": None
        # }
    }

    dados_clientes_json = json.dumps(dados_bancarios, ensure_ascii=False, indent=4)

    event = {
        "body": dados_clientes_json
    }
    context = None

    result = lambda_handler(event, context)
    logger.info("Resultado da execução do lambda_handler: %s", result)



