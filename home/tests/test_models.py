from django.test import TestCase
from home.models import *
from model_bakery import baker

class TestWriterModel(TestCase):
    def setUp(self):
        self.writer = baker.make(Writer, first_name='kevin', last_name='brown')

    def test_model_str(self):
        self.assertEqual(str(self.writer), 'kevin brown')