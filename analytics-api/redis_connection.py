import redis


class RedisConnection:
    
    @staticmethod
    def get_r_connection():
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        return r
    