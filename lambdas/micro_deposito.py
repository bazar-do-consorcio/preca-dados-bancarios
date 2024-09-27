import json
import requests
import logging
import os

from dotenv import load_dotenv
from datetime import datetime, timedelta

# Criação do logger e definição do nível de log
logger = logging.getLogger()
logger.setLevel(logging.INFO)


if not logger.hasHandlers():
    # Configuração do manipulador para saída no terminal
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)


load_dotenv()

LOGIN_API_HOST= os.getenv('LOGIN_API_HOST')
CONTACERTA_API_HOST= os.getenv('CONTACERTA_API_HOST')
CONTACERTA_API_CLIENT_ID= os.getenv('CONTACERTA_API_CLIENT_ID')
CONTACERTA_API_CLIENT_SECRET= os.getenv('CONTACERTA_API_CLIENT_SECRET')
USER_AGENT= os.getenv('USER_AGENT')

def lambda_handler(event, context):
    try:
        token_de_acesso, token_expirado = token_de_autorizacao(CONTACERTA_API_CLIENT_ID, CONTACERTA_API_CLIENT_SECRET, USER_AGENT)

        dados_bancarios = json.loads(event['body'])

        micro_deposito(dados_bancarios, token_de_acesso)

        return{
            'statusCode': 200,
            'body': json.dumps({'message': 'Dados processados com sucesso'})
        }
    except Exception as e:
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

    logger.info(f"Status code: {response.status_code}")
    logger.info(f"Response token_de_autorizacao: {response.text}")

    # Verificação do status da resposta
    if response.status_code != 200:
        raise Exception(f"Erro ao criar micro-deposito {response.status_code}, {response.text}")
    

    # Processamento do conteúdo da resposta, após a verificação do status
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

    logger.info(f"Status code: {response.status_code}")
    logger.info(f"Response micro_deposito: {response.text}")

    if response.status_code != 200:
        raise Exception(f"Erro ao criar micro-deposito {response.status_code}, {response.text}")
    return response.json().get('payload', {})


if __name__ == "__main__":
    dados_bancarios = {
        "name": "Fulana",
        "cpf_cnpj": "35271636598",
        "bank_code": "341",
        "agency": "7212",
        "account": "09708",
        "account_digit": "7",
        "account_type": "CONTA_CORRENTE",
        "pix_description": ""
    }

    dados_clientes_json = json.dumps(dados_bancarios, ensure_ascii=False, indent=4)

    event = {
        "body": dados_clientes_json
    }
    context = None

    result = lambda_handler(event, context)
    logger.info("Resultado da execução do lambda_handler: %s", result)



