# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 18:26
# @Author  : wenzhaoqing

import os
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LoveAndShare.settings")
    import django
    django.setup()
    from userinfo.models import *
    ret=UserInfo.objects.all().first()
    print(ret.username)