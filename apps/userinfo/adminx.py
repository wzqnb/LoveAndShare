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
    list_diaplay = ['title','body']




xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Article,ArticleAdmin)
