from pymongo import mongo_client
from config.settings import Settings

con = None

try:
    con = mongo_client.MongoClient(Settings.MONGO_URL, Settings.MONGO_PORT)
    print("Database Connected!")
except Exception as e:
    print(f"Error: {e}")


def getConnection():
    
    if con != None:
        connection = con
        return connection
    else:
        return "Wrong!"

getConnection()


