"""LoveAndShare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls import url
from django.views.static import serve
from LoveAndShare.settings import MEDIA_ROOT
from userinfo import views
import notifications.urls



urlpatterns = [
    path("admin/", admin.site.urls),
    # 评论通知
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    # 重置密码app
    path('password-reset/', include('password_reset.urls')),
    # home
    path("",views.index,name="Zindex"),
    # 搜索
    path("search/",include("haystack.urls")),
    path('accounts/', include('allauth.urls')),
    re_path("media/(?P<path>.*)", serve, {"document_root": MEDIA_ROOT}),
    path("userinfo/",include("userinfo.urls",namespace="userinfo")),
    path("article/",include("article.urls",namespace="article")),
    path("notice/",include("notice.urls",namespace="notice")),
    path("video/",include("video.urls",namespace="video")),

]

