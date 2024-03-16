from pymongo import MongoClient
conn = MongoClient("mongodb://localhost:27017")

# Creating new database students
db = conn['studentss']

# Creating new collection girls
collection = db['boyss']

# Inserting document into girls collection
collection.insert_one({"name": "Sarim", "age": 18})

print("Database and collection created with one document.")