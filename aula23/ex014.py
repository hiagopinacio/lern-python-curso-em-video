import requests
try:
    response = requests.get('http://www.pudim.com.br/')
    print(response.status_code)  # 200 significa requisição OK
except Exception as e:
    print(f'ERRO: {e}')