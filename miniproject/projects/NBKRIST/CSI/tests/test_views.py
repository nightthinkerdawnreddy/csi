from django.test import TestCase, Client
from django.urls import reverse
from CSI.models import Gallery,Photo
import json


class TestViews(TestCase):
    def setUp(self):
        self.Client=Client()
        self.home_url=reverse('home')
        self.about_url=reverse('about')
        self.officelist_url=reverse('officelist')
        self.snaps_url=reverse('snaps')
        self.past_url=reverse('past')

    def test_home_GET(self):
        response=self.client.get(self.home_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'CSI/home.html')

    def test_about_GET(self):
        response=self.client.get(self.about_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'CSI/about.html')

    def test_officelist_GET(self):
        response=self.client.get(self.officelist_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'CSI/officelist.html')

    def test_snaps_GET(self):
        response=self.client.get(self.snaps_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'CSI/snaps.html')

    def test_past_GET(self):
        response=self.client.get(self.past_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'CSI/past.html')
