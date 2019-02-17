import pymongo

#Servidor Mongo db
MONGO_SERVER = '104.131.97.10'
MONGO_PORT = 27017
MONGO_USERNAME = 'sistema'
MONGO_PASSWORD = '123@teste'
SOURCE = 'admin'

client = pymongo.MongoClient(MONGO_SERVER,MONGO_PORT)
mongodb = client.ecommerce
mongodb.authenticate(MONGO_USERNAME, MONGO_PASSWORD, source=SOURCE)



