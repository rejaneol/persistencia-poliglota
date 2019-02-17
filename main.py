"""
Trabalho final NOSQL
Tema: Ecommerce
Professor: Henrique Batista da Silva
Alunos:
		Tiago Henrique Zuim Queiroga
		Rejane Corrêa de Oliveira		

"""

###################################################################################
# Intruções para executar o script
#---------------------------------------------------------------------------------
#	Pelo prompt ou bash, acessar a pasta env/Scripts e executar o comando:
#	activate(Unix-Like) ou activate.bat(Windows)	
#   retornar a pasta raiz(Trabalho Final) e executar 'python main.py'
###################################################################################


###################################################################################
# O que deve ser feito e respondido no trabalho
###################################################################################
"""
	Deverá ser implementada uma solução para:
	a) Armazenamento de produtos e todas as suas características (atributos distintos) (FEITO)
	b) Armazenamento dos dados dos clientes, sendo que clientes possuem
	praticamente os mesmos atributos. (FEITO)
	c) Carrinho de compras: implementar uma solução adequada para armazenar o
	ID do cliente e os produtos que ele comprou. O banco escolhido deve ser
	rápido para tarefa de escrita e estar disponível a maior parte do tempo. Deve-se
	armazenar os produtos já vendidos.(FEITO)
	d) Sistema de recomendação de produtos. Sua solução deve ser capaz de
	recomendar um produto de acordo com o perfil de compra do cliente.
	
	Sua solução deve contemplar o uso de pelo menos 3 tipos de bancos NoSQL. Sua
	solução também deverá responder as seguintes perguntas:


	1. Qual o produto mais adicionando ao carrinho de compras em um determinado 
	momento.(FEITO)
	2. Listar dados de um determinado produto passado como consulta. (FEITO)

	3. Recomendar um produto para um determinado cliente: Para um cliente com o
		produto A no carrinho, responder a seguinte pergunta: Clientes que compraram
		o produto A também compraram o produto B, portanto, recomendar o produto
		B para o cliente.
"""


##################################################
# Bibliotecas utilizadas
##################################################
import json
import pprint
import sys
import sqlite3
import importador
import menu



#############################################################
# Importa os driver dos bancos
#############################################################
sys.path.append('drivers/mongodb')
sys.path.append('drivers/redis')
sys.path.append('drivers/neo4j')

# Drivers NOSQL
from mongodb_driver import mongodb
from redis_driver import redisdb
from neo4j_driver import neo4jdb
from neo4j_driver import neo4jdb2

# Driver Relacional
sqlite = sqlite3.connect('drivers/sqlite/database.db')


###############################################################################################
# Scripts(Models) - Contém o código relativo a cada modelo(Cliente,Produto,Carrinho,Compras)
###############################################################################################
sys.path.append('models')
import produtos
import clientes
import carrinhos
import recomendacoes




# Salvo os registros em seus respectivos bancos
def persistirBase():
	produtos.persiteProdutos(dados["produtos"])
	clientes.persiteClientes(dados["clientes"])
	carrinhos.persiteCarrinho(dados["carrinho"])
	recomendacoes.persiteRecomendacoes(dados["compras"])

# Inicio
if __name__ == "__main__":

	dados = importador.importaTodaBase()

	# Persistêcia dos dados
	persistirBase()

	# Mostra menu
	menu.principal()


