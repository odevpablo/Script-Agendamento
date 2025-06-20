import requests

# Endpoint e token
url = "https://backend-monitor.mottu.cloud/api/v1/Inadimplentes/servico/1177831"
token = "seu_token_aqui"

# Cabeçalho de autenticação
headers = {
    "Authorization": f"Bearer {token}"
}

# Fazendo a requisição
response = requests.get(url, headers=headers)

# Verificando a resposta
if response.status_code == 200:
    print("Sucesso:", response.json())
else:
    print(f"Erro {response.status_code}: {response.text}")
