import redis
from mongo_connection import MongoConnection as M
from datetime import datetime


class RedisConnection:
    
    @staticmethod
    def get_r_connection():
        r = redis.Redis(host='localhost', port=6379, decode_responses=True)
        return r
    
    @staticmethod
    def redis_poll():
        print('---pulling from urgent queue---\n')
        r = RedisConnection.get_r_connection()
        is_data = True
        while is_data:
            urgent_data = r.rpop('queue_urgent')
            if urgent_data:
                urgent_data['time_insertion'] = datetime.now()
                urgent_insert = M.insert_to_db(urgent_data)
                print(urgent_insert)
            else:
                normal_data = r.rpop('queue_normal')
                if normal_data:
                    normal_data['time_insertion'] = datetime.now()
                    normal_insert = M.insert_to_db(normal_data)
                    print(normal_data)
                else: # no more data
                    is_data = False
        return "no more data to insert"