from django.test import TestCase
from CSI.models import Photo


class TestModels(TestCase):
    def setUp(self):
        self.photos=Photo.objects.create(
        image='banner1.png',
        description="wonder"
        )
        
