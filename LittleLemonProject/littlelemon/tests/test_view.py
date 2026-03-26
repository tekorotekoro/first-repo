from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(APITestCase):
    @classmethod
    def setUp(cls):
        cls.item1 = Menu.objects.create(title="Rice", price=10.50, inventory=12)
        cls.item2 = Menu.objects.create(title="Shawama", price=5.50, inventory=10)

    def test_get_all_menu_items(self):
        url = reverse('menu_items')
        response = self.client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)