# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 10:57
# @Author  : wenzhaoqing


from haystack import indexes
from userinfo.models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().objects.all()