# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 18:26
# @Author  : wenzhaoqing

import os
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LoveAndShare.settings")
    import django
    django.setup()
    from userinfo.models import *
    from video.models import *
    id=1
    c = Course.objects.filter(id=id).first()
    print(c.title)
    print(c.pub_time)
    video_list = c.video_set.all()
    print(video_list)

