import pymongo

# connects to mongoDB server
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

mydb = myclient["mydb"]

my_collection = mydb["users"]
# Important: In MongoDB, a collection is not created until it gets content!

my_data = {"name" : "ankit", "username" : "user", "password" : "password"}

# insert data to collection

inserting = my_collection.insert_one(my_data)
# returns InsertOneResult object ID
print(inserting)