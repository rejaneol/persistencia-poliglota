# persistencia-poliglota
Um exercício de uma solução utilizando banco de dados relacionais e não-relacionais.

Projeto em parceria com Tiago Queiroga

Este é um pequeno exercício para criar uma solução de persistência poliglota. O enunciado do problema solicita uma solução para  a criação de um e-commerce, que atenda às seguintes especificações:  
a) Armazenamento de produtos e todas as suas características (atributos distintos)  
b) Armazenamento dos dados dos clientes, sendo que clientes possuem praticamente os mesmos atributos.  
c) Carrinho de compras: implementar uma solução adequada para armazenar o ID do cliente e os produtos que ele comprou. O banco escolhido deve ser rápido para tarefa de escrita e estar disponível a maior parte do tempo. Deve-se armazenar os produtos já vendidos.   
d) Sistema de recomendação de produtos. A solução deve ser capaz de recomendar um produto de acordo com o perfil de compra do cliente. 
 
A solução contempla o uso um banco de dados relacional (MySQL) para o cadastro de clientes e 3 tipos de bancos NoSQL: 
- um banco do tipo documento (MongoDB) para o cadastro e consultad de produtos;  
- um banco do tipo chave-valor (Redis) para o carrinho de compras;
- um banco do tipo grafos (Neo4j) para o sistema de recomendação ("quem viu A também viu B; quem comprou C também comprou D")

A solução objetiva responder as seguintes perguntas: 
 
1. Qual o produto mais adicionando ao carrinho de compras em um determinado momento. 
2. Listar dados de um determinado produto passado como consulta. 
3. Recomendar um produto para um determinado cliente: Para um cliente com o produto A no carrinho, responder a seguinte pergunta: Clientes que compraram o produto A também compraram o produto B, portanto, recomendar o produto B para o cliente. 

O arquivo Trabalho Final NOSQL.pdf dá as instruções sobre como utilizar a solução.
