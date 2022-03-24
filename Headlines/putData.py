
import pymongo  # for mongodb access
import pandas as pd

# Establish connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Import the csv files
db = client.Headlines
business = pd.read_csv('Headlines/business.csv')
entertainment = pd.read_csv('Headlines/entertainment.csv')
general=pd.read_csv('Headlines/general.csv')
health=pd.read_csv('Headlines/health.csv')
science=pd.read_csv('Headlines/science.csv')
sports=pd.read_csv('Headlines/sports.csv')
technology=pd.read_csv('Headlines/technology.csv')

data = business.to_dict(orient='records')
db.business.insert_many(data)

data = entertainment.to_dict(orient='records')
db.entertainment.insert_many(data)

data = general.to_dict(orient='records')
db.general.insert_many(data)

data = health.to_dict(orient='records')
db.health.insert_many(data)

data = science.to_dict(orient='records')
db.science.insert_many(data)

data = sports.to_dict(orient='records')
db.sports.insert_many(data)

data = technology.to_dict(orient='records')
db.technology.insert_many(data)