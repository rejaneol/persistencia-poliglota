import json
import inspect
from main import neo4jdb as neo4j
from main import neo4jdb2 as neo4j2
from main import pprint

# Pega todos os clientes que vem do model Clientes(SQLite)
import clientes as clientes_model
# Pega todos os clientes que vem do model Produtos(Mongodb)
import produtos as produtos_model
# Pega todos os carrinhos que vem do model Carrinhos(Redis)
import carrinhos as carrinhos_model

from neo4jrestclient import client

def criaLabelCliente():
	cliente_node = neo4j.labels.create("cliente")
	clientes = clientes_model.pegaClientes();
	for cliente in clientes:
		clt = neo4j.nodes.create(
			id = str(cliente[0]), 
			nome = cliente[1], 
			email = cliente[2], 
			cidade = cliente[3], 
			estado = cliente[4],
			data_nascimento = cliente[5]
		)
		cliente_node.add(clt)

def criaLabelProduto():
	produto_node = neo4j.labels.create("produto")
	produtos = produtos_model.pegaProdutos({})

	for produto in produtos:
		prd = neo4j.nodes.create(
			prod_id = str(produto["prod_id"]),
			nome = produto["nome"], 
			marca = produto["marca"], 
			modelo = produto["modelo"], 
			preco=produto["preco"]
		)
		produto_node.add(prd)	


def limpaBase():
	q = 'MATCH (n) OPTIONAL MATCH (n)-[rel]-() DELETE rel, n'
	neo4j.query(q)

def persiteRecomendacoes(compras):
	print("\tSalvando recomendações no banco Neo4j")
	# Limpa a base neo4j caso tenha algum registro anterior a execução do script
	limpaBase()

	# Cria base neo4j
	criaLabelCliente()
	criaLabelProduto()	
	criaRelacaoCompra(compras)


# Relacao Produto x Cliente
def criaRelacaoCompra(compras):
	for compra in compras:
		p = neo4j2.labels.get("produto")
		c = neo4j.labels.get("cliente")

		cliente = c.get(id=compra["cliente"])
		produto = p.get(prod_id=compra["produto"])

		cliente[0].relationships.create("compra", produto[0])
	

def listaTodasCompras():
	print("\n ******** Todas as compras realizadas ******** ")
	q = 'MATCH (c:cliente)-[r:compra]->(p:produto) RETURN c, type(r), p'
	results = neo4j.query(q, returns=(client.Node, str, client.Node))
	for r in results:
	    print("(%s)-[%s]->(%s)" % (r[0]["nome"], "Comprou", r[2]["nome"]))


def recomendaOutroProduto(carrinho_cliente,prod_id):
	recomendacoes = []
	produto_origem = None;

	# Produto Origem
	q = """
			MATCH (p:produto) 
			WHERE p.prod_id = '{prod_id}' 
			RETURN p.nome as produto limit 1
			""".format(prod_id=prod_id)
	results = neo4j.query(q, returns=(str))
	for r in results:
		produto_origem = r[0]

	# Recomendacao
	q = """
			MATCH (c:cliente)-[r:compra]->(p:produto) 
			MATCH   (c:cliente)-[or:compra]->(p:produto) 
			WHERE c.id = '{carrinho_cliente}' and  p.prod_id <> '{prod_id}' 
			RETURN p.nome as recomendacao
			""".format(carrinho_cliente=carrinho_cliente,prod_id=prod_id)
	results = neo4j.query(q, returns=(str))


	for r in results:
		recomendacoes.append({"tambem_compra":r[0]})

	if produto_origem == None:
		print("\t \n Produto não existe")

	else:
		print("\t *** Recomendação do produto(" + str(produto_origem) + ") ***")
		for recomendacao in recomendacoes:
			if recomendacao["tambem_compra"] != None and len(recomendacao) > 0:
				recomenda = "Quem compra '{compra}' também compra '{tambem_compra}'".format(compra=produto_origem,tambem_compra=recomendacao["tambem_compra"])
				print(recomenda)
			else:
				print("\t Não existe recomendações para este produto")