from redis import Redis

from core.config import settings

redis_host = 'localhost'
r = Redis(host=redis_host, socket_connect_timeout=1) # short timeout for the test

r.ping()

print('connected to redis "{}"'.format(redis_host))