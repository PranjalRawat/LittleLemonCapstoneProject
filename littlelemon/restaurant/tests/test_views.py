import json
from django.test import TestCase
from restaurant.models import Menu
from django.core.serializers import serialize
import requests

class MenuViewTest(TestCase):
    def setup(self):
        self.item1 = Menu.objects.create(id=4, title="Cream", price=20, inventory=25)
        self.item2 = Menu.objects.create(id=5, title="Pasta", price=180, inventory=50)

    def test_getall(self):
        response = requests.get('http://127.0.0.1:8000/restaurant/menu/menu/')

        if response.status_code == 200:
            # Parse the JSON data from the response
            external_data = response.json()

        print(external_data)