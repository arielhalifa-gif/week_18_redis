from mongo_connection import MongoConnection as M


class DataAcces:

    @staticmethod
    def q1():
        pass


    @staticmethod
    def top_urgent_zones():
        collection = M.get_mongo_collection()
        resultq2 = collection.find([
            {"$match": {'priority': 'URGENT'}},
            {"$group": {"_id": 'zone'},
             'count': {'$sum': 1}},
             {'$sort': {'zone': -1}},
             {'$limit': 5}
        ])
        return resultq2
    


    @staticmethod
    def q3():
        pass