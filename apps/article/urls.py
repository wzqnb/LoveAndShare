# -*- coding: utf-8 -*-
# @Time    : 2019/10/2 14:47
# @Author  : wenzhaoqing

from django.urls import path
from . import views
app_name = 'article'
urlpatterns = [
    path('article_detail/<int:id>/',views.article_detail,name='article_detail'),
    path('article_category/<str:category>/',views.article_category,name='article_category'),
    path('article_tag/<str:tag>/',views.article_tag,name='article_tag'),
    path('article_archive/',views.article_archive,name='article_archive'),
    path('article_updown/',views.article_updown,name='article_updown'),


]

