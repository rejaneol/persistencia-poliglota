import json
from main import redisdb as redis
from main import pprint

import itertools
import operator

carrinho_redis_prefix = 'carrinho_cliente_'

def clientId(id):
	return 'carrinho_cliente_' + str(id)

def pegaChavesTodosCarrinhos():
	return redis.keys(carrinho_redis_prefix + "*")

def persiteCarrinho(carrinho):
	print("\tSalvando carrinho em banco Redis")
	for car in carrinho:
		# Salva a chave com o formato 'carrinho_cliente_#cliente'
		cliente = clientId(car['idCliente']) 
		pedidos = json.dumps(car['itensPedido'])
		redis.set(cliente,pedidos)

def listaCarrinho(cliente = None):
	# Lista Todos
	if(cliente == None):
		print("\n ******** Carrinhos ******** ")
		for carrinho in listaTodosCarrinhos():
			print("\n Carrinho Cliente(" + carrinho["idCliente"] + ")")
			for pedido in json.loads(carrinho["pedidos"]):
				print("\t ID Produto:" + str(pedido["prod_id"]) + "  Nome:" + str(pedido["nomeProduto"]))


	# Lista Carrinho especificado de cliente
	else:
		print("\n ******** Carrinho Cliente (" + str(cliente) + ") ******** ")
		carrinho = redis.get(clientId(cliente))
		if carrinho is None:
			print("\tCarrinho não encontrado")
		else:
			carrinho = json.loads(carrinho)
			for pedido in carrinho:
				print("\t ID Produto:" + str(pedido["prod_id"]) + "  Nome:" + str(pedido["nomeProduto"]))


def listaTodosCarrinhos():
	chaves = pegaChavesTodosCarrinhos()
	carrinhos = []
	for chave in chaves:
		carrinho = redis.get(chave)
		cliente = chave.replace(carrinho_redis_prefix,'')
		carrinhos.append({
			"idCliente":cliente,
			"pedidos":carrinho
		})
	return carrinhos	
	

def produtosMaisAdicionados():
	carrinhos = listaTodosCarrinhos()
	produtos = [];
	for carrinho in carrinhos:
		carrinho_json = json.loads(carrinho["pedidos"])
		for pedido in carrinho_json:
			produtos.append("ID:" + str(pedido["prod_id"]) + " - Nome:" + pedido["nomeProduto"])
	pprint.pprint("Produto mais adicionado é: " + maisComumEmLista(produtos))


def maisComumEmLista(L):
  # get an iterable of (item, iterable) pairs
  SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
  groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
  def _auxfun(g):
    item, iterable = g
    count = 0
    min_index = len(L)
    for _, where in iterable:
      count += 1
      min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
    return count, -min_index
  # pick the highest-count/earliest item
  return max(groups, key=_auxfun)[0]