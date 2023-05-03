import pymongo

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017")

mydb = myclient["mydb"]

mycol = mydb["users"]

# without argument, gives first document(record)
x = mycol.find_one()
print(x)

# takes argument which matches with document
x = mycol.find_one({"_id":1})

print(x)