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
    path('test/',views.test,name='test'),
    path('get_img_captcha/',views.get_img_captcha,name='get_img_captcha'),
    path('get_phonecaptcha/',views.get_phonecaptcha,name='get_phonecaptcha'),
    path('check_phone_exist/',views.check_phone_exist,name='check_phone_exist'),

]
