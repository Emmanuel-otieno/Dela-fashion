from django.urls import path
from .views import Home,Cart,Checkout,OrderView
from .auth import LoginCheckMiddleware,LogoutCheckMiddleware
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',Home.as_view(), name='home'),
    path('cart',Cart.as_view(), name='cart'),
#    path('signup',LogoutCheckMiddleware(Signup.as_view()), name='signup'),
#    path('login',LogoutCheckMiddleware(Login.as_view()), name='login'),
#    path('logout',LoginCheckMiddleware(logout), name='logout'),
    path('checkout',LoginCheckMiddleware(Checkout.as_view()), name='checkout'),
    path('order',LoginCheckMiddleware(OrderView.as_view()), name='order'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)