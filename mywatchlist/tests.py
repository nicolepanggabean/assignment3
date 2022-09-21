from django.test import TestCase, Client

# Create your tests here.
# source: https://docs.djangoproject.com/en/4.1/topics/testing/tools/

class WatchlistTest(TestCase):
    def __init__(self):
        self.client = Client()
    
    def htmlTest(self):
        response = self.client.get('mywatchlist/html/')
        self.assertEqual(response.status_code, 200)

    def xmlTest(self):
        response = self.client.get('mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def jsonTest(self):
        response = self.client.get('mywatchlist/json/')
        self.assertEqual(response.status_code, 200)