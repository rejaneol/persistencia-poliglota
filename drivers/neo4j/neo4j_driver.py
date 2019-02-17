from neo4jrestclient.client import GraphDatabase

#Servidor Neo4j
NEO4JS_SERVER = 'http://104.131.97.10:7474'
NEO4JS_USERNAME = 'neo4j'
NEO4JS_PASSWORD = 'theCLASH1908'

neo4jdb = GraphDatabase(NEO4JS_SERVER, username=NEO4JS_USERNAME, password=NEO4JS_PASSWORD)
neo4jdb2 = GraphDatabase(NEO4JS_SERVER, username=NEO4JS_USERNAME, password=NEO4JS_PASSWORD)
