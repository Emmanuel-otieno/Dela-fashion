from django.urls import path
from .views import Home,Cart,Checkout,OrderView
from .auth import LoginCheckMiddleware,LogoutCheckMiddleware


urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('cart',Cart.as_view(), name='cart'),
    path('checkout',LoginCheckMiddleware(Checkout.as_view()), name='checkout'),
    path('order',LoginCheckMiddleware(OrderView.as_view()), name='order'),
]
