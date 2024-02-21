from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(id=3, title="Ice Cream", price=80, inventory=25)
        self.assertEqual(str(item), "Ice Cream : 80")
