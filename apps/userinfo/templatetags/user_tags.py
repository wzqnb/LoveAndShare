# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 13:29
# @Author  : wenzhaoqing

from django import template
from userinfo.models import Article,Category,Tag

register=template.Library()

@register.inclusion_tag("article_views.html")
def get_article_view():
    article_list=Article.objects.all().order_by("-views")[0:5]
    print("article_list",article_list)

    return {
        "article_list":article_list,
    }


@register.inclusion_tag("article_category.html")
def get_article_category():
    article_category=Category.objects.all()
    return {
        "article_category":article_category
    }


@register.inclusion_tag("tagscloud.html")
def get_article_tags():
    article_tags=Tag.objects.all()
    return {
        "article_tags": article_tags
    }

@register.inclusion_tag("recently_article.html")
def get_recently_article():
    recently_article=Article.objects.all().order_by("-pub_time")[0:5]
    print(recently_article)
    return {
        "recently_article": recently_article
    }
