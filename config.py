import os


class Config:
    '''
    General configuration parent class
    '''
    pass
NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
NEWS_APIKEY = os.environ.get('NEWS_APIKEY')
NEWS_SECRET_KEY = os.environ.get('NEWS_SECRET_KEY')
# BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
# ARTICLE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'

staticmethod
def init_app():
    pass


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
config_options = {
'development': DevConfig,
'production': ProdConfig
}