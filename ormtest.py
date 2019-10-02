# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 18:26
# @Author  : wenzhaoqing

import os
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LoveAndShare.settings")
    import django
    django.setup()
    from userinfo.models import *

    # c=Category.objects.filter(name="python").first()
    # print(c)
    # obj=c.article_set.all()
    # print(obj)


    tag=Tag.objects.filter(title="python").first()
    print(tag)
    obj_tag=tag.article_set.all()
    print(obj_tag)
    # for


