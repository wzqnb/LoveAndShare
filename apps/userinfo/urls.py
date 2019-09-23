# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 18:57
# @Author  : wenzhaoqing
from django.urls import path
from . import views
app_name = 'userinfo'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('login/',views.login,name="login"),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),

]
