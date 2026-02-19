import redis


class RedisConnection:
    
    def get_r_connection():
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        return r
    
    @staticmethod
    def redis_queue_priority(priority_data, queue_name):
        r = RedisConnection.get_r_connection()

        r.lpush(queue_name, priority_data)