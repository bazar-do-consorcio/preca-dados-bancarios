import json
import logging


# Criação do logger e definição do nível de log
logger = logging.getLogger()
logger.setLevel(logging.INFO)


if not logger.hasHandlers():
    # Configuração do manipulador para saída no terminal
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)


def lambda_handler(event, context):
   
    try:
        return processar_webhook_resposta(event['body'])
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps("Erro interno no servidor. Verifique os logs para mais detalhes.")
        }
    

def processar_webhook_resposta(body):
    resposta = json.loads(body)

    # Cenário de Sucesso
    validacao_data = resposta['data']

    if validacao_data.get('valid') is True:

        #... aqui vc colocs as ações no cenário que der sucesso

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Conta validada com sucesso',
                'status': validacao_data.get('micro_deposit_status', 'STATUS_DESCONHECIDO'),
                'deposit_method': validacao_data.get('micro_deposit_method', 'METODO_DESCONHECIDO')
            })
        }
    
    else:
        # Cenário de erro
        erros = validacao_data.get('errors', [])

        #... aqui vc colocs as ações no cenário que der erro

        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'Falha na validação dos dados',
                'errors': erros
            })
        }

if __name__ == "__main__":
    dados_bancarios = {
    "id": "7d3aae40-6655-4d9a-801b-d0ab7ae906d7",
    "version": "v1",
    "object": "Validation",
    "date": "2019-10-01T17:54:39.000Z",
    "data": {
        "id": "8f9d9bb5-119e-4da8-bd50-3418d227c1d6",
        "integration_id": None,
        "micro_deposit_status": "VALIDADO",
        "micro_deposit_value": None,
        "micro_deposit_method": "TRANSFERENCIA",
        "valid": True,
        "errors": [],
        "receipt_url": None,
        "bank_receipt_url": None,
        "pix_description": None,
        "source": "API",
        "created_at": "2019-10-25T17:33:56.000Z",
        "person_type": "natural_person",
        "person_type_details": {
            "natural_person": {
                "is_under_age": False
            }
        }
    }
}

    dados_clientes_json = json.dumps(dados_bancarios, ensure_ascii=False, indent=4)

    event = {
        "body": dados_clientes_json
    }
    context = None

    result = lambda_handler(event, context)
    logger.info("Resultado da execução do lambda_handler: %s", result)



