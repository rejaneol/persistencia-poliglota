import sys
import os
###############################################################################################
# Importando models do main.py
###############################################################################################
from main import produtos
from main import clientes
from main import carrinhos 
from main import recomendacoes


def limpaTela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')    

def principal():
    escolha ='0'
    while True:
        print("\n\n **** Menu Principal ****")
        print("(1) Produto (Mongodb)")
        print("(2) Cliente (SQLite - Relacional)")
        print("(3) Carrinho (Redis)")
        print("(4) Recomendação (Neo4j)")
        print("(0) Para Sair")
        escolha = input (":")

        if escolha == "5":
            print("Go to another menu")
            second_menu()
        elif escolha == "4":
            menuRecomendacoes()
        elif escolha == "3":
            menuCarrinhos()
        elif escolha == "2":
            menuClientes()
        elif escolha == "1":
            menuProdutos()
        elif escolha == "0":
            exit()    
        else:
            principal()

def menuProdutos():
    print("\n\n **** Menu Produtos ****")
    print("(*) Todos Produtos")
    print("(1-999) Produto Especifico")
    print("(0) Voltar Menu Principal")

    escolha = input ("prod_id:")

    # Lista todos os produtos no banco(Mongodb)
    if escolha == "*":
        produtos.listaProdutos({}) 
        menuProdutos()
    
    if escolha == "0":
        limpaTela()
        principal()

    else:
        produtos.listaProdutos({"prod_id":escolha})
        menuProdutos()


def menuClientes():
    print("\n\n **** Menu Clientes ****")
    print("(*) Todos Clientes")
    print("(1-999) Cliente Especifico")
    print("(0) Voltar Menu Principal")

    escolha = input ("id:")

    # Lista todos os produtos no banco(Mongodb)
    if escolha == "*":
        clientes.listaClientes()
        menuClientes()
    
    if escolha == "0":
        limpaTela()
        principal()

    else:
        clientes.listaClientes(escolha)
        menuClientes()

def menuCarrinhos():
    print("\n\n **** Menu Carrinhos ****")
    print("(*) Todos Carrinhos")
    print("(1-999) Carrinho Cliente Especifico")
    print("(+) Ver Produto mais adicionado")
    print("(0) Voltar Menu Principal")

    escolha = input ("Cliente ID:")

    # Lista todos
    if escolha == "*":
        carrinhos.listaCarrinho()
        menuCarrinhos()


    if escolha == "+":
        carrinhos.produtosMaisAdicionados()
        menuCarrinhos()
    
    if escolha == "0":
        limpaTela()
        principal()

    else:
        carrinhos.listaCarrinho(escolha)
        menuCarrinhos()

def menuRecomendacoes():
    print("\n\n **** Menu Recomendações ****")
    print("(1) Compras Realizadas ")
    print("(2) Recomendacões de Produto")
    print("(0) Voltar Menu Principal")

    escolha = input (":")

    if escolha == "1":
        recomendacoes.listaTodasCompras()
        menuRecomendacoes()

    if escolha == "2":
        carrinhos.listaCarrinho()
        escolha_carrinho = input ("Carrinho do Cliente Exemplo(4):")
        escolha_produto = input ("Produto no Carrinho Exemplo(4):")
        recomendacoes.recomendaOutroProduto(str(escolha_carrinho),str(escolha_produto))
        menuRecomendacoes()        
    
    if escolha == "0":
        limpaTela()
        principal()

    else:
        menuRecomendacoes()        

if __name__ == "__main__":
    principal()