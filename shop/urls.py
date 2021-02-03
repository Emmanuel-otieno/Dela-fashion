from django.urls import path




urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('cart',Cart.as_view(), name='cart'),
]