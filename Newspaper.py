
from newspaper import Article
import newspaper
import nltk
nltk.download('punkt')

api_key= '0e97cac02d994073b9a7d649b05e16f7'
categories = ["business","entertainment","general","health","science","sports","technology"]
    
for list in categories:

    url = ('http://newsapi.org/v2/top-headlines?'
            'country=in&'
             'category='+list+'&'
            'language=en&'
            'apiKey=' + api_key)


class MainSource(newspaper.Source):
    def __init__(self, articleURL):
        super(MainSource, self).__init__('http://localhost')
        self.articles = [newspaper.Article(url=articleURL)]


sources = [MainSource(articleURL=u) for u in URLS]

newspaper.news_pool.set(sources)
newspaper.news_pool.join()

Final_Summary = ""
for src in sources:
    src.articles[0].download()
    src.articles[0].parse()
    src.articles[0].nlp()
    Final_Summary += src.articles[0].summary + "\n"
    print('Title:', src.articles[0].title)
    print('Author:', src.articles[0].authors)


Final_Summary = Final_Summary[:-1]
print('Summary:', Final_Summary)
