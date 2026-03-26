from django.test import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.menu = Menu.objects.create(
            title = "Pasta",
            price = 12.99,
            inventory = 10
        )

    def test_string_representation(self):
        self.assertEqual(str(self.menu), "Pasta - 12.99")