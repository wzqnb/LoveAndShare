# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 14:35
# @Author  : wenzhaoqing

import xadmin
from .models import *
from xadmin import views

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "LoveAndShare"
    site_footer = "1843326800@qq.com"


class ArticleAdmin(object):
    list_display = ["id","title","desc","author","category","pub_time","views","up_count","down_count",]
    search_fields=["title","author","category","pub_time",]
    list_filter=["id","title","body","author","category","pub_time","views","up_count","down_count",]
    list_editable=["id","title","desc","category","views","up_count","down_count",]

class TagAdmin(object):
    list_display=["title",]

class CategroyAdmin(object):
    list_display = ["name", ]

class BlogSettingAdmin(object):
    list_display = ["id", "title", "body", "author", "category", "pub_time", "views", "up_count", "down_count", ]
    search_fields = ["title", "author", "category", "pub_time", ]





xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Category,CategroyAdmin)
