from requests import get

BASE_URL = "https://api.etherscan.io/api"

data = get(make_api_url(module="account", action="balance", address="0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae", tag="latest"))

#recebe address e tag como parametro, retorna base_url + url
make_api_url() 

get_balance_byAddress()

get_last_block()

#tests
print(data)
print("Separação") #oq interessa é o result=
print(data.json())