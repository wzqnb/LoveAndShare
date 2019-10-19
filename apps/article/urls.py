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
    path('comment/',views.comment,name='comment'),
    path('article_add/',views.article_add,name='article_add'),
    path('article_image_upload/',views.article_image_upload,name='article_image_upload'),
    path('article_list_forme/<int:pk>/',views.article_list_forme,name='article_list_forme'),
    path('article_detele/',views.article_detele,name='article_detele'),
    path('article_editor/<int:id>/',views.article_editor,name='article_editor'),
    path('article_editor_save/',views.article_editor_save,name='article_editor_save'),
    path('article_collect/',views.article_collect,name='article_collect'),
    path('article_collect_list/<int:id>/',views.article_collect_list,name='article_collect_list'),
    path('article_collect_detele/',views.article_collect_detele,name='article_collect_detele'),


]

