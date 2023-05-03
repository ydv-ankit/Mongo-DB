import pymongo

# connects to mongoDB server
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

mydb = myclient["mydatabase"]

# list available databases
databases = myclient.list_database_names()

# lets check if db "mydb" exists
target_db = "mydb"
if target_db in databases:
    print(target_db + " exists")
else:
    print(target_db + " doesn't exists")
