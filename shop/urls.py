from django.urls import path
from .views import Home,Cart,Checkout



urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('cart',Cart.as_view(), name='cart'),
]