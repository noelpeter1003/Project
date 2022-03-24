from django.shortcuts import render
# Create your views here.
import pandas as pd
import pymongo  # for mongodb access
import pandas as pd
import requests

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
general=[]
Entertainment=[]
business=[]
health=[]
science=[]
sports=[]
technology=[]
# Create a database
def putData():
    
# Establish connection
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)

# Import the csv files
    db = client.Headlines
    business = pd.read_csv('business.csv')
    entertainment = pd.read_csv('entertainment.csv')
    general=pd.read_csv('general.csv')
    health=pd.read_csv('health.csv')
    science=pd.read_csv('science.csv')
    sports=pd.read_csv('sports.csv')
    technology=pd.read_csv('technology.csv')

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

def getData():
    categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
    for list in categories:

        url = ('http://newsapi.org/v2/top-headlines?'
            'country=us&'
            'category=' + list + '&'
                                'language=en&'
                                'apiKey=a6514dbbe8bb4c559910baeaf5c2a848')
        urlResponse = requests.get(url)
        urlResponse = urlResponse.json()

        articles = []
        for item in urlResponse['articles']:
            dict = {

                "title": item['title'],
             "urlToImage": item['urlToImage'],
             "description": item['description']
            }
            articles = articles + [dict]

        conn = "mongodb://localhost:27017"
        client = pymongo.MongoClient(conn)

        if len(articles) > 0:
            df = pd.DataFrame(urlResponse['articles'])
            df = df.loc[:, ["title", "urlToImage"]]
            df.to_csv(list + '.csv')
def delData():
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
def extractData():
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)
    db = client.Headlines

    hG = pd.DataFrame(db.general.find())

    count=1
    global general
    for (i,j) in zip(hG.title,hG.urlToImage):

        general=general+[
        {"id":count,"name":i,"image":j},
        ]
        count=count+1

    hG = pd.DataFrame(db.entertainment.find())

    count=1
    global Entertainment

    for (i,j) in zip(hG.title,hG.urlToImage):
        Entertainment=Entertainment+[
        {"id":count,"name":i,"image":j},
        ]
    
        count=count+1


    hG = pd.DataFrame(db.business.find())

    count=1
    global business
    for (i,j) in zip(hG.title,hG.urlToImage):
        business=business+[
        {"id":count,"name":i,"image":j},
        ]
    
        count=count+1



    hG = pd.DataFrame(db.health.find())
    count=1
    global health
    for (i,j) in zip(hG.title,hG.urlToImage):
        health=health+[
        {"id":count,"name":i,"image":j},
        ]
    
        count=count+1

    hG = pd.DataFrame(db.science.find())
    count=1
    global science
    for (i,j) in zip(hG.title,hG.urlToImage):
        science=science+[
        {"id":count,"name":i,"image":j},
        ]
    
        count=count+1


    hG = pd.DataFrame(db.sports.find())
    count=1
    global sports
    for (i,j) in zip(hG.title,hG.urlToImage):
        sports=sports+[
        {"id":count,"name":i,"image":j},
        ]
    
        count=count+1


    hG = pd.DataFrame(db.technology.find())
    count=1
    global technology
    for (i,j) in zip(hG.title,hG.urlToImage):
        technology=technology+[
        {"id":count,"name":i,"image":j},
        ]
    
        count=count+1


def home(request):
    delData()
    getData()
    putData()
    extractData()
    return render(request,'home.html',{'general_headlines':general,'entertainment_headlines':Entertainment,'business':business,'health':health,'science':science,'sports':sports,'technology':technology})
def summarize(request,pk):
    return render(request,'summarize.html')


