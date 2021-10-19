from django.urls import path
from order import views

urlpatterns = [
    path('addtoshopcart/<int:id>', views.add_to_shopcart, name='addtoshopcart'),
    path('shopcart/', views.shopcart, name='shopcart'),
]