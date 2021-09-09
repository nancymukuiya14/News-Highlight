class Config:
    '''
    General configuration parent class
    '''
    pass
NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
NEWS_APIKEY = 'd0054354f7a3447581e739eb8be8abd4'
NEWS_SECRET_KEY = 'secret'

staticmethod
def init_app(app):
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