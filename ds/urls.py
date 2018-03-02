from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('user/',include('ds_user.urls'),name='user'),
    path('order/',include('ds_order.urls'),name='order'),
    path('cart/',include('ds_cart.urls'),name='cart'),

    path('',include('ds_goods.urls'),name='goods'),
]
