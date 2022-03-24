import pandas as pd
import pymongo

import requests

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

    print(articles)
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)

    if len(articles) > 0:
        df = pd.DataFrame(urlResponse['articles'])
        df = df.loc[:, ["title", "urlToImage"]]
        df.to_csv('Headlines/' + list + '.csv')
