import redis

#Servidor Redis
REDIS_SERVER = '104.131.97.10'
REDIS_PORT = 6379

redisdb = redis.StrictRedis(
		host=REDIS_SERVER, 
		port=REDIS_PORT, 
		charset="utf-8", 
		decode_responses=True, db=0
)




