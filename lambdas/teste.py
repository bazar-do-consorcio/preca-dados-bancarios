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

def lambda_handler(event):
    # Obter a URL pré-assinada
    url_pre_assinada = obter_url_pre_assinada(id_organizacao, nome_arquivo)
    logger.info(f"URL pré-assinada obtida: {url_pre_assinada}")

    # Extrair o caminho formatado da URL
    caminho_formatado = extrair_caminho(url_pre_assinada)
    logger.info(f"Caminho formatado: {caminho_formatado}")

    # Fazer o upload do arquivo
    arquivo_url = 'https://api-sandbox.transfeera.com/pub/receipt/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFuc2Zlcl9pZCI6IjE0NTcwMzMiLCJyZWNlaXB0X3R5cGUiOiJ0cmFuc2ZlZXJhIiwiYmF0Y2hfdHlwZSI6IlRSQU5TRkVSRU5DSUEiLCJpYXQiOjE3Mjc3MTkzNTksImV4cCI6MTczMjkwMzM1OX0.sdgChnHOdEApu_36NsScrhAIU3ExoyBqc-KZLffjuEY'
    sucesso_upload = fazer_upload(url_pre_assinada, arquivo_url)
    if sucesso_upload:
        logger.info("Upload realizado com sucesso.")

        # Atualizar o campo no Pipefy com o caminho formatado
        resposta_atualizacao = atualizar_campo_pipefy(card_id, campo_id, caminho_formatado)
        logger.info(f"Resposta da atualização: {resposta_atualizacao}")
    else:
        logger.error("Falha ao realizar o upload do arquivo.")

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


def atualizar_campo_pipefy(card_id, campo_id, caminho_arquivo):
    url = 'https://api.pipefy.com/graphql'
    headers = {
        "Authorization": f"Bearer {PIPEFY_TOKEN}",
        "Content-Type": "application/json"
    }
    mutation = f"""
    mutation {{
        updateCardField(input: {{ card_id: {card_id}, field_id: "{campo_id}", new_value: ["{caminho_arquivo}"] }}) {{
            clientMutationId
            success
        }}
    }}
    """
    response = requests.post(url, headers=headers, json={'query': mutation})
    return response.json()

if __name__ == "__main__":
    id_organizacao = '301247725'  
    nome_arquivo = 'Comprovante_Micro_Deposito.pdf'  
    card_id = '971537587'  # ID do card
    campo_id = 'comprovante_microdep_sito'  # ID do campo

    context = None

    event = {}  

    result = lambda_handler(event)
    logger.info("Resultado da execução do lambda_handler: %s", result)
