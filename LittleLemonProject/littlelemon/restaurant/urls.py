from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu-items', views.MenuItemView.as_view(), name='menu_items'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu_item'),
    path('api-token-auth/', obtain_auth_token),
]