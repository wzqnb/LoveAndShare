# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 14:50
# @Author  : wenzhaoqing

from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [

    path('course_token/', views.course_token, name='course_token'),
    path('course/', views.course, name='course'),
    path('course_detail/<int:id>/', views.course_detail, name='course_detail'),

]

