import requests
import os
import logging
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Configuração de logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

if not logger.hasHandlers():
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)

# Caminho para o certificado e chave privada
certificado_prod = (
    r'C:\Users\kelly.vasconcellos_b\Develop\transfeera\preca-dados-bancarios\21b133c6-2179-470e-80c2-b1859950ce22.crt',
    r'C:\Users\kelly.vasconcellos_b\Develop\transfeera\preca-dados-bancarios\private.key'
)

load_dotenv()

LOGIN_API_HOST = os.getenv('LOGIN_API_HOST')
CONTACERTA_API_HOST = os.getenv('CONTACERTA_API_HOST')
CONTACERTA_API_CLIENT_ID = os.getenv('CONTACERTA_API_CLIENT_ID')
CONTACERTA_API_CLIENT_SECRET = os.getenv('CONTACERTA_API_CLIENT_SECRET')
USER_AGENT = os.getenv('USER_AGENT')

# Função para obter o token de autorização
def obter_token():
    """Função para obter o token de autorização usando client credentials com mTLS."""
    url = f'{LOGIN_API_HOST}/authorization'

    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "grant_type": "client_credentials",
        "client_id": CONTACERTA_API_CLIENT_ID,
        "client_secret": CONTACERTA_API_CLIENT_SECRET
    }

    try:
        # Fazer a requisição para obter o token com mTLS
        response = requests.post(url, headers=headers, json=payload, cert=certificado_prod)

        # Verificar se a resposta foi bem-sucedida
        if response.status_code == 200:
            token = response.json().get('access_token')
            logger.info(f"Token obtido com sucesso: {token}")
            return token
        else:
            logger.error(f"Erro ao obter token: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao fazer requisição: {str(e)}")
        return None

# Função para criar o microdepósito
def criar_microdepósito(payload, token):
    url = f"{CONTACERTA_API_HOST}/validate?type=MICRO_DEPOSITO"  # Endpoint de microdepósito

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": USER_AGENT,
    }

    try:
        # Fazer a requisição usando mTLS
        response = requests.post(url, headers=headers, json=payload, cert=certificado_prod)

        if response.status_code == 200:
            logger.info("Microdepósito criado com sucesso!")
        else:
            logger.error(f"Erro ao criar microdepósito: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao fazer requisição para criar microdepósito: {str(e)}")

# Exemplo de payload
payload = {
    "name": "Transfeera Pagamentos",
    "cpf_cnpj": "27084098000169",
    "bank_code": "237",
    "agency": "2232",
    "account": "40",
    "account_type": "CONTA_CORRENTE",
    "integration_id": "",
    "account_digit": "8"
}

# Chamada de teste para obter o token e criar o microdepósito
token = obter_token()
if token:
    criar_microdepósito(payload, token)
else:
    logger.error("Falha ao obter o token, não foi possível criar o microdepósito.")
