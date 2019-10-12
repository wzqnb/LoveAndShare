# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 14:50
# @Author  : wenzhaoqing

from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    # path('list/', views.list, name='list'),
    # path('update/', views.CommentNoticeUpdateView.as_view(), name='update'),
# path('list/', views.list, name='list'),
# path('update/', views.update, name='update'),
path('list/', views.CommentNoticeListView.as_view(), name='list'),
    path('update/', views.CommentNoticeUpdateView.as_view(), name='update'),
    # path('update/', views.CommentNoticeUpdateView.as_view(), name='update'),

]

