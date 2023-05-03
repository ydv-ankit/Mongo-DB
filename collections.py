import pymongo

# connects to mongoDB server
myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

mydb = myclient["mydb"]

my_collection = mydb["users"]
# Important: In MongoDB, a collection is not created until it gets content!

# my_data = {"name" : "ankit", "username" : "user", "password" : "password"}

# insert data to collection

# inserting = my_collection.insert_one(my_data)
# returns InsertOneResult object ID, which is inserted automatically by mongoDB if not specified
# print(inserting.inserted_id)

# to insert many data items
# my_data2 = [
#     {"name": "Amy", "address": "Apple st 652"},
#     {"name": "Hannah", "address": "Mountain 21"},
#     {"name": "Michael", "address": "Valley 345"},
#     {"name": "Sandy", "address": "Ocean blvd 2"},
#     {"name": "Betty", "address": "Green Grass 1"},
#     {"name": "Richard", "address": "Sky st 331"},
#     {"name": "Susan", "address": "One way 98"},
#     {"name": "Vicky", "address": "Yellow Garden 2"},
#     {"name": "Ben", "address": "Park Lane 38"},
#     {"name": "William", "address": "Central st 954"},
#     {"name": "Chuck", "address": "Main Road 989"},
#     {"name": "Viola", "address": "Sideway 1633"},
# ]

# many = my_collection.insert_many(my_data2)

# returns multiple IDs as many documents are inserted
# print(many.inserted_ids)

with_id = my_collection.insert_one({"_id":30, "name":"yadav", "address" : "out of range"})

print(with_id.inserted_id)
