
# coding: utf-8

# In[1]:


from neo4jrestclient.client import GraphDatabase


# In[2]:


from neo4jrestclient import client


# In[3]:


#conectando ao banco de dados de grafos
db = GraphDatabase("http://localhost:7474", username="neo4j", password="123")


# In[5]:


#apagando o banco de dados de grafos
#q = 'MATCH (n) OPTIONAL MATCH (n)-[rel]-() DELETE rel, n'
#db.query(q)

#esse comando não funciona dentro do Python


# In[6]:


#criando o tipo de nodo "usuario" 
user = db.labels.create("usuario")


# In[7]:


#criando os nodos do tipo "usuario" com seus atributos    
u1 = db.nodes.create(name="Bob", email = 'bob@email', data_nascimento = '01/12/1984', cidade='BH', estado='MG')
u2 = db.nodes.create(name="Alice", email = 'alice@email', data_nascimento = '25/11/1985', cidade='BH', estado='MG')
u3 = db.nodes.create(name="Lea", email = 'lea@email', data_nascimento = '13/05/1989', cidade='BH', estado='MG')
u4 = db.nodes.create(name="Ana", email = 'joel@email', data_nascimento = '10/01/1985', cidade='BH', estado='MG')
u5 = db.nodes.create(name="Joel", email = 'ana@email', data_nascimento = '01/10/1988', cidade='BH', estado='MG')


# In[8]:


# associando os nós ao tipo "usuario"
user.add(u1, u2, u3, u4, u5)


# In[9]:


person = db.labels.get("usuario")
person.all()


# In[10]:


for c in person.all():
    print(c)


# In[11]:


#consultando os nós do label "usuario"
q = 'MATCH (n:usuario) RETURN n'
results = db.query(q, data_contents=True)
results.rows


# In[12]:


#criando o tipo de nodo "produto" 
prod = db.labels.create("produto")


# In[13]:


#criando os nodos do tipo "produto" com seus atributos
p1 = db.nodes.create(prod_id=1, preco=49.90,nome='Pendrive',marca='Marca',modelo="modelo")
p2 = db.nodes.create(prod_id=2, preco=35.00,nome='Cartão Micro SD',marca='Marca',modelo="modelo")


# In[14]:


# associando os nós ao tipo "produto"
prod.add(p1, p2)


# In[15]:


#consultando os nós do label "produto"
q = 'MATCH (n:produto) RETURN n'
results = db.query(q, data_contents=True)
results.rows


# In[16]:


#criando os relacionamentos entre os nós (inventados por mim)
u1.relationships.create("compra", p1)
u2.relationships.create("compra", p1)
u2.relationships.create("compra", p2)
u3.relationships.create("compra", p2)


# In[21]:


#obtendo os dados sobre "compra"

q = 'MATCH (u:usuario)-[r:compra]->(p:produto) RETURN u, type(r), p'
results = db.query(q, returns=(client.Node, str, client.Node))

QuemCompra = []
for r in results:
    QuemCompra.append(r[0]["name"]) 
    print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["nome"]))


# In[23]:


#obtendo os produtos que Bob comprou

q = 'MATCH (u:usuario)-[r:compra]->(p:produto) WHERE u.name="Bob" RETURN p'
results2 = db.query(q, returns=(client.Node))

BobCompra = []
for r in results2:
    BobCompra.append(r[0]["nome"]) 

print('Bob comprou ', len(BobCompra), 'produto(s):', BobCompra)


# In[24]:


# acessando o primeiro produto que Bob comprou
primeiro = BobCompra[0]
print(primeiro)


# In[28]:


#identificando quem comprou o mesmo produto que Bob (apenas o primeiro produto)
q = 'MATCH (u:usuario)-[r:compra]->(p:produto) WHERE p.nome="' + primeiro + '" RETURN u'
results3 = db.query(q, returns=(client.Node))


# In[30]:


#imprimindo os usuarios que também compraram o primeiro produto que Bob comprou (incluindo Bob):
PrimeiroCompra = []
for r in results3:
    PrimeiroCompra.append(r[0]["name"]) 

for i in PrimeiroCompra:
    print (i)


# In[31]:


# identificando outros produtos comprados pelos usuarios que compraram também o primeiro produto de Bob:

ComprouTambem = []

for user in PrimeiroCompra:
    if user != 'Bob':
        q = 'MATCH (u:usuario)-[r:compra]->(p:produto) WHERE u.name="' + user + '" RETURN p'
        results4 = db.query(q, returns=(client.Node))
        for r in results4:
            if (r[0]["nome"]) != primeiro:
                ComprouTambem.append(r[0]["nome"]) 
        

print('Quem comprou ', primeiro, 'comprou também', ComprouTambem)

