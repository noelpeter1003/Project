import requests
from newspaper import Article
import newspaper
import nltk
nltk.download('punkt')

def getUrls():
    api_key= '0e97cac02d994073b9a7d649b05e16f7'
    url = 'https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey='+ api_key
    news= requests.get(url).json()

    articles= news["articles"]

    urls=[]
    my_news= ""

    for article in articles :
        urls.append(article["url"])

    return urls

urls = getUrls()

class MainSource(newspaper.Source):
    def __init__(self, articleURL):
        super(MainSource, self).__init__('http://localhost')
        self.articles = [newspaper.Article(url=articleURL)]


sources = [MainSource(articleURL=u) for u in urls]

newspaper.news_pool.set(sources)
newspaper.news_pool.join()

Final_Summary = ""
for src in sources:
    if len(src.articles) > 0:
        src.articles[0].download()
        src.articles[0].parse()
        src.articles[0].nlp()
        
        print('Title:', src.articles[0].title)
        print('Author:', src.articles[0].authors)
        print('summary:' ,src.articles[0].summary)


#Final_Summary = Final_Summary[:-1]
# print('Summary:', Final_Summary)
 

