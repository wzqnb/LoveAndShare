# -*- coding: utf-8 -*-
# @Time    : 2019/10/5 15:52
# @Author  : wenzhaoqing
import re

import cgi
import html
from bs4 import BeautifulSoup
c= html.escape('', quote=True)

print(c)
print("hhhhhhhhhhhhhhhhhh")
# v=html.unescape(c)

def xssfilter(s):
    if not s :
        return s

    text=[]
    for i in s:
        # print(i)
        def switch_test_item(item):
            switcher = {
                '&': "&amp;",
                '<': "&lt;",
                '>': "&gt;",
                '"': "&quot;",
                '\'': "&#x27;",
                '/':"&#x2F;",
            }
            text.append(switcher.get(i, i))
        switch_test_item(i)
    return "".join(text)

h="<h1>ggggggggggggg</h1>"

# c=xssfilter(h)
# print(c)
cc= html.escape(h, quote=True)
print(cc)

f=["fff","dfdf"]

for i in f:
    print(i)



