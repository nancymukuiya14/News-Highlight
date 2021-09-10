from app.models.news import news
import unittest
from app.models import News
news = news.news()

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News()

    
if __name__ == '__main__':
    unittest.main()