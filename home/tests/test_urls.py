from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import *

class TestUrls(SimpleTestCase):
    def test_home(self):
        url = reverse('home:home') #/
        self.assertEquals(resolve(url).func, home)

    def test_about(self):
        url = reverse('home:about', args=('narges',)) #/about/narges
        self.assertEquals(resolve(url).func, about)