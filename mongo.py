import pymongo

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

mydb = myclient["mydatabase"]
