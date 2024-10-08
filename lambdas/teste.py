import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# URL do Pipefy e token de autorização
URL_PIPEFY = os.getenv('URL_PIPEFY')
PIPEFY_TOKEN = os.getenv('PIPEFY_TOKEN')

# Função para consultar o Pipefy
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
    
    headers = {
        "Authorization": f"Bearer {PIPEFY_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(URL_PIPEFY, json={"query": query}, headers=headers)

    if response.status_code == 200:
        data = response.json()
        nodes = data.get("data", {}).get("findCards", {}).get("nodes", [])

        if nodes:
            return nodes[0]
        print("Card não encontrado no Pipefy.")
    else:
        print(f"Erro ao buscar card no Pipefy: {response.status_code} - {response.text}")

    return None

# Exemplo de uso
transfeera_id = "ea793454-9f0e-4ff6-8d6b-12813c4d64db"  # Substitua pelo ID que deseja buscar
card = consultar_card_no_pipefy(transfeera_id)

if card:
    print("Card encontrado:")
    for field in card["fields"]:
        print(f"{field['name']}: {field['value']}")
else:
    print("Card não encontrado.")
