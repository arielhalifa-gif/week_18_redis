from pymongo import MongoClient


class MongoConnection:

    @staticmethod   
    def connect_to_mongo():
        uri = "mongodb://localhost:27017/"
        client = MongoClient(uri)

        try:
            
            client.admin.command("ping")
            print("Connected successfully")
        except Exception as e:
            client.close()
            raise Exception(
               "The following error occurred: ", e)
        return client

    @staticmethod
    def get_mongo_collection():
        client = MongoConnection.connect_to_mongo()
        db = client['week-18-db']
        collection = db['border-alerts']
        return collection