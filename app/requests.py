import urllib.request
import json
from .models import Articles, Sources


BASE_SOURCE_URL = None
BASE_ARTICLE_URL = None
BASE_SEARCH_URL = None
# get api_key
api_key = None


def configure_request(app):
    global api_key,BASE_SOURCE_URL,BASE_ARTICLE_URL,BASE_SEARCH_URL
    api_key = app.config['API_KEY']
    BASE_SEARCH_URL = app.config['SEARCH_URL']
    BASE_ARTICLE_URL = app.config['ARTICLE_URL']
    BASE_SOURCE_URL = app.config['SOURCE_URL']

def get_source():
    news_source_url = BASE_SOURCE_URL.format(api_key)
    with urllib.request.urlopen(news_source_url) as news_source:
        source_data = news_source.read()
        source_data_dict = json.loads(source_data)
        
        sources_results = None
        
        if source_data_dict['sources']:
            sources_list = source_data_dict['sources']
            sources_results = process_sources(sources_list)
        
        return sources_results
    
def process_sources(sources):
    sources_list = []
    for source in sources:
        id = source['id']
        name = source['name']
        description = source['description']
        url = source['url']
        country = source['country']
        language = source['language']
        category = source['category']
        
        if url:
            source_object = Sources(id,name,description,url,country,language,category)
            sources_list.append(source_object)
            
    return sources_list

def get_news_articles(id):
    articles_url = BASE_ARTICLE_URL.format(id, api_key)
    with urllib.request.urlopen(articles_url) as articles:
        articles_data = articles.read()
        articles_data_dict = json.loads(articles_data)
        
        articles_results = None
        
        if articles_data_dict['articles']:
            articles_list = articles_data_dict['articles']
            articles_results = process_articles_data(articles_list)
            
        return articles_results
    
    
def process_articles_data(data):
    articles_results = []
    for article in data:
        image = article['urlToImage']
        description = article['description']
        time = article['publishedAt']
        url = article['url']
        title = article['title']
        author = article['author']
        
        if time:
            articles_object = Articles(image, description, time,url, title, author)
            articles_results.append(articles_object)
            
    return articles_results
    
    
def search_news(phrase):
    search_news_url = BASE_SEARCH_URL.format(phrase, api_key)
    with urllib.request.urlopen(search_news_url) as search_news:
        search_news_data = search_news.read()
        search_news_data_dict = json.loads(search_news_data)
        
        search_news_results = None
        
        if search_news_data_dict['articles']:
            search_news_list = search_news_data_dict['articles']
            search_news_results = process_articles_data(search_news_list)
            
    return search_news_results