#Imports

from requests import get

	- get é uma função que recebe como argumento uma url. Responsável por realizar a chamada de api ou "request"
	- .json() é um método p transformar essa informação em formato json (pré existente em python nativo)


#Variables

BASE_URL = "https://api.etherscan.io/api"
 	- Toda chamada de api começa com essa url base


#Functions

make_api_url()
	- Uma função que recebe os parâmetros p/ chamada de api e retorna a url específica p cada chamada
	Exemplo

	make_api_url(address="0xasidj182dias...",tag=latest) -> BASE_URL + x

get_balance_byAddress()
	- Função responsável por retornar o saldo de uma carteira específica


get_last_block()
	- Retorna o último bloco lançado na blockchain

