import json
import requests
import logging
import os
import re
import boto3

from dotenv import load_dotenv
from datetime import datetime, timedelta

logger = logging.getLogger()
logger.setLevel(logging.INFO)

if not logger.hasHandlers():
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)

load_dotenv()

LOGIN_API_HOST= os.getenv('LOGIN_API_HOST')
CONTACERTA_API_HOST= os.getenv('CONTACERTA_API_HOST')
CONTACERTA_API_CLIENT_ID= os.getenv('CONTACERTA_API_CLIENT_ID')
CONTACERTA_API_CLIENT_SECRET= os.getenv('CONTACERTA_API_CLIENT_SECRET')
USER_AGENT= os.getenv('USER_AGENT')
URL_PIPEFY = os.getenv('URL_PIPEFY')

id_webhook = None


def obter_cabecalhos():
    if os.getenv('ENVIRONMENT') == 'development':
        secret_token = os.getenv('PIPEFY_TOKEN')
    else:
        # Cria cliente para Secrets Manager
        client = boto3.client('secretsmanager', region_name='us-east-1')
        
        # Recupera o segredo
        secret_name = 'secret_tokens'
        try:
            response = client.get_secret_value(SecretId=secret_name)
            secret = json.loads(response['SecretString'])
            secret_token = secret['pipefy_token']
        except Exception as e:
            logger.error("Erro ao recuperar o segredo %s ", str(e), exc_info=True)
            raise

    return {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {secret_token}'
    }


def tratar_dados_bancarios(dados_bancarios):
    # Extrair apenas os três primeiros dígitos do código do banco
    bank_match = re.match(r'(\d{3})', dados_bancarios['bank'])
    if bank_match:
        dados_bancarios['bank'] = bank_match.group(1)
    else:
        raise ValueError("O código do banco deve ter exatamente 3 dígitos.")
    
    # Tratar o campo 'account' para separar a conta do dígito verificador
    account_match = re.match(r'(\d+)-?(\d)?', dados_bancarios['account'])
    if account_match:
        dados_bancarios['account'] = account_match.group(1)  # Número da conta
        # Extrair o dígito se houver, caso contrário, deixar como string vazia
        dados_bancarios['account_digit'] = account_match.group(2) if account_match.group(2) else dados_bancarios['account'][-1]
        dados_bancarios['account'] = dados_bancarios['account'][:-1]  # Remover o último dígito (verificador) da conta
    
    return dados_bancarios


def lambda_handler(event, context):
    try:
        token_de_acesso, token_expirado = token_de_autorizacao(CONTACERTA_API_CLIENT_ID, CONTACERTA_API_CLIENT_SECRET, USER_AGENT)

        dados_bancarios = json.loads(event['body'])

        # Tratar o campo "bank" para obter apenas o número e renomeá-lo para "bank_code"
        bank_number = dados_bancarios['bank'].split(' ')[0]
        dados_bancarios['bank_code'] = bank_number
        del dados_bancarios['bank']  # Remove o campo 'bank', já que é substituído por 'bank_code'

        # Tratar o campo "account" para separar o número da conta do dígito
        conta = dados_bancarios['account']
        if '-' in conta:
            numero_conta, digito_conta = conta.split('-')
        else:
            numero_conta, digito_conta = conta[:-1], conta[-1]

        dados_bancarios['account'] = numero_conta
        dados_bancarios['account_digit'] = digito_conta

        # Transformar "account_type" em maiúsculo
        dados_bancarios['account_type'] = dados_bancarios['account_type'].upper()

        # LOG - Verificar os dados bancários tratados antes de enviar o microdepósito
        logger.info(f"Dados bancários tratados: {json.dumps(dados_bancarios, ensure_ascii=False, indent=4)}")

        # Criar o micro depósito usando os dados tratados
        resultado_micro_deposito = micro_deposito(dados_bancarios, token_de_acesso)
        micro_deposito_id = resultado_micro_deposito.get('id')

        # Salvar id do micro depósito no card do pipefy
        salvar_id = atualizar_campo_transfeera_id(971537587, micro_deposito_id)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Dados processados com sucesso',
                'micro_deposito_id': micro_deposito_id
            })
        }

    except Exception as e:
        logger.error(f"Erro ao processar os dados: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps("Erro interno no servidor. Verifique os logs para mais detalhes.")
        }

   
def token_de_autorizacao(CONTACERTA_API_CLIENT_ID, CONTACERTA_API_CLIENT_SECRET, USER_AGENT):
    url = f'{LOGIN_API_HOST}/authorization'

    headers = {
        "User-Agent": USER_AGENT,
        "Content-Type": "application/json"
    }

    payload = {
        "grant_type": "client_credentials",
        "client_id": CONTACERTA_API_CLIENT_ID,
        "client_secret": CONTACERTA_API_CLIENT_SECRET
    }

    response = requests.post(url, headers=headers, json=payload)

    logger.info(f"Response token_de_autorizacao:  {response.status_code}, {response.text}")

    if response.status_code != 200:
        raise Exception(f"Erro ao criar micro-deposito {response.status_code}, {response.text}")
    
    info_token = response.json()

    token = info_token.get('access_token')
    expira_em = info_token.get('expires_in', 0)

    prazo_de_validade = datetime.now() + timedelta(seconds=expira_em)

    return token, prazo_de_validade


def micro_deposito(payload, token):
    url = f'{CONTACERTA_API_HOST}/validate?type=MICRO_DEPOSITO'

    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": USER_AGENT,
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, headers=headers, json=payload)

    logger.info(f"Response micro_deposito: {response.status_code}, {response.text}")

    if response.status_code != 200:
        raise Exception(f"Erro ao criar micro-deposito {response.status_code}, {response.text}")
    
    response_data = response.json()
    # Campo 'id' dentro de 'payload':
    response_data.get('payload', {}).get('id')

    return response_data


def atualizar_campo_transfeera_id(node_id, transfeera_id):
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
    variables = {
        "nodeId": str(node_id),
        "values": [
            {
                "fieldId": "transfeera_id",  
                "value": transfeera_id    
            }
        ]
    }

    response = requests.post(URL_PIPEFY, json={'query': mutation, 'variables': variables}, headers=obter_cabecalhos())

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao atualizar o campo no Pipefy: {response.status_code}, {response.text}")



if __name__ == "__main__":
    dados_bancarios = {
        # "node_id": "971537587",
        "name": "Transfeera Pagamentos",
        "cpf_cnpj": "27084098000169",
        "bank": "237 - Banco ABC",
        "agency": "2232",
        "account": "406058",
        "account_type": "conta_corrente",
        "integration_id": ""
    }

    dados_clientes_json = json.dumps(dados_bancarios, ensure_ascii=False, indent=4)

    event = {
        "body": dados_clientes_json
    }
    context = None

    result = lambda_handler(event, context)
