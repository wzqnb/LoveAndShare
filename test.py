# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 15:07
# @Author  : wenzhaoqing
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# font_path = os.path.join(BASE_DIR, 'static', 'verdana.ttf')
font_path = os.path.join(os.path.dirname(__file__))
print(font_path)

import memcache
mc = memcache.Client(['127.0.0.1:11211'], debug=0)
# mc.set("some_key", "Some value")
# value = mc.get("some_key")
# print(value)
# mc.set("another_key", 3)
# mc.delete("another_key")
# mc.set("key", "1")   # note that the key used for incr/decr must be a string.
# mc.incr("key",10)
# print(mc.get("key"))
# mc.decr("key")
# mc.set("wen","1111")
# print(mc.get("wen"))
# mc.set_multi({"q":"ww","w":"ee"},time=60*2)
# print(mc.get("w"))

from django.core.cache import cache

from django.core.cache import cache


# from utils import captcha
#
# c=captcha.Captcha.gene_code()
# print(c)
from utils.captcha import PhoneCaptcha
c=PhoneCaptcha()
print(c.get_code())