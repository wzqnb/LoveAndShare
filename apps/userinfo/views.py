from django.shortcuts import render,HttpResponse,redirect,reverse
from django.views.decorators.http import require_POST,require_GET
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from utils.captcha import Captcha
from utils import restful
from django.contrib.auth import get_user_model

User=get_user_model()

def index(request):
    return HttpResponse("hello")


def login(requset):
    pass


def register(request):
    '''用户注册'''
    if request.method=="POST":
        pass




def logout(request):
    pass