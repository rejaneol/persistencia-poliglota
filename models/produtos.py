import json
import inspect
from main import mongodb
from main import pprint


def persiteProdutos(produtos):
	print("\tSalvando produtos em banco Mongodb")
	# Limpa collection
	mongodb.produtos.remove({})

	#Converte o dicionário de produtos para string JSON
	produtos_string = json.dumps(produtos)

	# Cria o collection com os produtos
	produtos = json.loads(produtos_string)
	mongodb.produtos.insert(produtos)


def pegaProdutos(find):
	produto = mongodb.produtos.find(find)
	return produto

def listaProdutos(find):
	if(find == {}):
		print("\n ******** Produtos ******** ")
	else:
		print("\n ******** Produto(" + find["prod_id"] + ") ******** ")

	produtos = pegaProdutos(find)
	for produto in produtos:
		pprint.pprint(produto)