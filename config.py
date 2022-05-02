import os

class Config:
    SOURCE_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    ARTICLE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    SEARCH_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    API_KEY = os.environ.get('API_KEY')
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True\
        
config_options = {
'development':DevConfig,
'production':ProdConfig
}