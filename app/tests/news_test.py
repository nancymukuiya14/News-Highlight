from ..models import news, news_article
import unittest
news = news.news()

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = news()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,news))
        
        
    
# if __name__ == '__main__':
#     unittest.main()