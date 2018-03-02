from ds_user.views import *
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login',views.login,name='login'),
    path('Regist',views.Regist,name='Regist'),
    path('reg',views.register_handle,name='reg'),
    path('logout',logout),
    path('log_hand',login_handle),
    path('checkname',register_exist),
    path('userinfo',user_center_info),
    path('userupdate',userupdate),
    path('shdz',shdz),
    path('add_save',add_save),
    path('mrdz', mrdz),
    path('scdz', scdz),
    path('bjdz', bjdz),
]

