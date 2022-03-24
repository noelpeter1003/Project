print("Demonstration python based mongodb access");


import pymongo              # for mongodb access
import pprint               # for pretty printing db data

#Let's get the user object from the db

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Create a database
db = client.Headlines

db.business.delete_many({})
db.entertainment.delete_many({})
db.general.delete_many({})
db.health.delete_many({})
db.science.delete_many({})
db.sports.delete_many({})
db.technology.delete_many({})
