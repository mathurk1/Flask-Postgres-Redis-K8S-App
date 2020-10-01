from redis import Redis

redis = Redis(host='redis-service', port=6379)

redis.incr('hits')

cnt = redis.get('hits').decode("utf-8")

print(cnt)