# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 13:29
# @Author  : wenzhaoqing

from django import template
from userinfo.models import *

register=template.Library()

@register.simple_tag
def simple_tag_multi(v1,v2):
    return  v1*v2

