import hashlib
from django.shortcuts import render
from LoveAndShare import settings
import time
import os
import hmac
from utils import restful
from .models import *

# Create your views here.

def course(request):
    course_detail = Course.objects.all()
    return render(request, "video/course.html", {"course_detail": course_detail})

def course_detail(request,id):
    pass

def course_token(request):
    # video：是视频文件的完整链接
    file = request.GET.get('video')
    expiration_time = int(time.time()) + 2 * 60 * 60

    USER_ID = settings.Baibu_User_Id
    USER_KEY = settings.Baibu_User_Key

    # file=http://hemvpc6ui1kef2g0dd2.exp.bcevod.com/mda-igjsr8g7z7zqwnav/mda-igjsr8g7z7zqwnav.m3u8
    extension = os.path.splitext(file)[1]
    media_id = file.split('/')[-1].replace(extension, '')
    key = USER_KEY.encode('utf-8')
    message = '/{0}/{1}'.format(media_id, expiration_time).encode('utf-8')
    signature = hmac.new(key, message, digestmod=hashlib.sha256).hexdigest()
    token = '{0}_{1}_{2}'.format(signature, USER_ID, expiration_time)
    return restful.result(data={'token': token})
