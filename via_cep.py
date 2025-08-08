import requests as requests
import json as json

cep = input("Digite o CEP: ")
cep_tratado = cep.replace('-', '').replace('.', '').replace(' ', '')
endpoint = 'https://viacep.com.br/ws/'
url = endpoint + cep_tratado + '/json/'

payload = {}
headers = {}

response = requests.get(url)

if str(response.status_code).startswith('2'):
    dados = response.json()
    
    if dados.get('erro'):
        print("CEP inválido ou não encontrado.")
    else:

      cep = dados.get('cep', '')
      logradouro = dados.get('logradouro', '')
      complemento = dados.get('complemento', '')
      unidade = dados.get('unidade', '')
      bairro = dados.get('bairro', '')
      localidade = dados.get('localidade', '')
      uf = dados.get('uf', '')
      estado = dados.get('estado', '')
      regiao = dados.get('regiao', '')
      ibge = dados.get('ibge', '')
      gia = dados.get('gia', '')
      ddd = dados.get('ddd', '')
      siafi = dados.get('siafi', '')
        
      print(
          f"Cep: {cep_tratado}" "\n"
          f"Logradouro: {logradouro}" "\n"
          f"Complemento: {complemento}" "\n"
          f"Unidade: {unidade}" "\n"
          f"Bairro: {bairro}" "\n"
          f"Localidade: {localidade}" "\n"
          f"UF: {uf}" "\n"
          f"Estado: {estado}" "\n"
          f"Região: {regiao}" "\n"
          f"IBGE: {ibge}" "\n"
          f"GIA: {gia}" "\n"
          f"DDD: {ddd}" "\n"
          f"SIAFI: {siafi}" "\n"
          f"Maps: https://www.google.com/maps/place/{logradouro.replace(' ', '+')}+{bairro.replace(' ', '+')}+{localidade.replace(' ', '+')}+{uf}"
      )
else:
    print(f"CEP inválido ou não encontrado: {response.status_code}")