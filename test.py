# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 15:07
# @Author  : wenzhaoqing
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# font_path = os.path.join(BASE_DIR, 'static', 'verdana.ttf')
font_path = os.path.join(os.path.dirname(__file__))
print(font_path)