import requests

from acesso_cep import BuscaEndereco

cep = "25800320"
objeto_cep = BuscaEndereco(cep)

# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(r.text)

a = objeto_cep.acessa_via_cep()
print(type(a.text))
print(a.json())
print(a.json()["cep"])
print(a.json()["bairro"])
