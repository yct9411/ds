from ds_goods.views import *
# from django.contrib import admin
from django.urls import path,re_path
urlpatterns = [
    re_path('^(\d+)$',detail),
    re_path('^list_(\d+)_(\d+)_(\d+)$',typelist),
    path('', index, name='index'),

]

