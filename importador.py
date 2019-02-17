import json
import csv
import sys

def importaTodaBase():
	print("\tImportando bases do diretório 'bases/ecommerce')")
	return  {
		"carrinho":importaCarrinho('bases/ecommerce/carrinho.json'),
		"clientes":importaClientes('bases/ecommerce/clientes.txt'),
		"compras":importaCompras('bases/ecommerce/compras.csv'),
		"produtos":importaProdutos('bases/ecommerce/produtos.txt')
	}

# Importa carrinho de compras
def importaCarrinho(caminho):
	return json.load(open(caminho))

# Importa clientes
def importaClientes(caminho):
	dados = []
	with open(caminho, newline='') as csvfile:
	    leitor = csv.reader(csvfile, delimiter=',')
	    for linha in leitor:
	    	dados.append({
	    		"id":int(linha[0]),
	    		"nome":linha[1],
	    		"email":linha[2],
	    		"data_nascimento":linha[3],
	    		"cidade":linha[4],
	    		"estado":linha[5],
	    	})
	return dados	

# Importa compras
def importaCompras(caminho):
	dados = []
	with open(caminho, newline='') as csvfile:
	    leitor = csv.reader(csvfile, delimiter=',')
	    next(leitor, None)  # Ignora cabecalho
	    for linha in leitor:
	    	dados.append({
	    		"cliente":linha[0],
	    		"produto":linha[1],
	    	})
	return dados    	

# Importa Produtos
def importaProdutos(caminho):
	dados = []
	with open(caminho, newline='') as csvfile:
	    leitor = csv.reader(csvfile, delimiter=',')
	    for linha in leitor:
	    	dados.append({
	    		"prod_id":linha[0],
	    		"preco":linha[1],
	    		"nome":linha[2],
	    		"marca":linha[3],
	    		"modelo":linha[4],
	    		"categoria":linha[5]
	    	})	
	return dados    	