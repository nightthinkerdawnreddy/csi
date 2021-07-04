from django.test import SimpleTestCase
from django.urls import resolve, reverse
from CSI.views import home,about,officelist,snaps,past

class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func, home)
    def test_list_url_is_resolved(self):
        url=reverse('about')
        self.assertEquals(resolve(url).func, about)
    def test_list_url_is_resolved(self):
        url=reverse('officelist')
        self.assertEquals(resolve(url).func, officelist)
    def test_list_url_is_resolved(self):
        url=reverse('snaps')
        self.assertEquals(resolve(url).func, snaps)
    def test_list_url_is_resolved(self):
        url=reverse('past')
        self.assertEquals(resolve(url).func, past)
