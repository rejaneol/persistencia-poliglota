import json
from main import sqlite
from main import pprint


def persiteClientes(clientes):
	criaTabelaClientes()
	salvaClientes(clientes);
	#sqlite.close()

def criaTabelaClientes():
	cursor = sqlite.cursor()
	cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (id int, nome text, mail text, 
														   cidade text, estado text, 
														   data_nascimento text)
				   ''')

def salvaClientes(clientes):
	print("\tSalvando clientes em banco SQLite")
	# Transforma a lista de dicionario(clientes) para o formato do insert(sqlite)
	registros = []
	for cliente in clientes:
		registros.append(
							(
							  cliente['id'],
							  cliente['nome'],
						 	  cliente['email'],
						 	  cliente['cidade'],
						 	  cliente['estado'],
						 	  cliente['data_nascimento']
						 	)
						)

	sqlite.executemany('INSERT INTO clientes VALUES (?,?,?,?,?,?)', registros)

def pegaClientes(id = None):
	# Todos
	if id == None:
		query = "SELECT * FROM clientes ORDER BY id"
	else:
		query = "SELECT * FROM clientes WHERE id =" + str(id) + " ORDER BY id"

	cursor = sqlite.cursor()
	clientes = cursor.execute(query)
	return clientes	

def listaClientes(id = None):
	print("\n ******** Clientes ******** ")
	clientes = pegaClientes(id)
	for cliente in clientes:
		pprint.pprint(cliente)
