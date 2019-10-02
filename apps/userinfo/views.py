from django.shortcuts import render, HttpResponse, redirect, reverse
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from utils.captcha import ImgCaptcha, PhoneCaptcha
from utils import restful
from utils import yunpian
from django.contrib import auth
from io import BytesIO
from django.http import JsonResponse
from .models import *
from .forms import RegForm
from django.contrib.auth import get_user_model
import base64
from utils.pager import PageInfo

User = get_user_model()


def test(request):
    import os
    import string

    # Captcha验证码
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    font_path = os.path.join(BASE_DIR, 'static', 'verdana.ttf')

    from PIL import Image, ImageDraw, ImageFont
    import random

    def get_random_color():
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    # 生成一个图片对象
    img_obj = Image.new(
        'RGB',
        (220, 35),
        get_random_color()
    )
    # 在生成的图片上写字符
    # 生成一个图片画笔对象
    draw_obj = ImageDraw.Draw(img_obj)
    # 加载字体文件， 得到一个字体对象
    font_obj = ImageFont.truetype("../../static/verdana.ttf", 28)
    # 开始生成随机字符串并且写到图片上
    tmp_list = []

    def tmp():
        return "j"
    for i in range(4):


        draw_obj.text((20 + 40 * i, 0), tmp(), fill=get_random_color(), font=font_obj)

    print("".join(tmp_list))
    print("生成的验证码".center(120, "="))
    from io import BytesIO
    io_obj = BytesIO()
    # 将生成的图片数据保存在io对象中
    img_obj.save(io_obj, "png")
    # 从io对象里面取上一步保存的数据
    data = io_obj.getvalue()
    data = base64.b64encode(data).decode()
    return render(request,"test.html",{"data":data})



def index(request):
    count=Article.objects.all().count()
    page_info = PageInfo(request.GET.get('page'), count, 8, 'userinfo/index/', 11)
    article_list = Article.objects.all()[page_info.start():page_info.end()]




    return render(request, "index.html",{"article_list":article_list,'page_info':page_info})


def login(request):
    '''用户登陆'''

    if request.method == "POST":
        username = request.POST.get("username")
        print("username:", username)
        password = request.POST.get("password")
        valid_code = request.POST.get("valid_code")
        print("valid_code:", valid_code)
        if valid_code and valid_code.lower() == cache.get(valid_code.lower()):
            print("验证码正确")
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return restful.ok(data=reverse("userinfo:index"))
            else:
                return restful.params_error(message="账号或密码错误")
        else:
            return restful.params_error(message="验证码错误")

    return render(request, "login.html")


def get_phonecaptcha(request):
    '''获取手机验证码'''
    ret = {"status": 0, "msg": ""}
    phone = request.POST.get("phone")
    print("取得电话：", phone)
    code = PhoneCaptcha().get_code()
    print("code:", code)
    cache.set(phone, code, 5 * 60)
    ret["msg"] = code
    return JsonResponse(ret)


def get_img_captcha(request):
    '''获取图片验证码'''
    text, image = ImgCaptcha.gene_code()
    cache.set("code", text, 5 * 60)
    # BytesIO：相当于一个管道，用来存储图片的流数据
    out = BytesIO()
    # 调用image的save方法，将这个image对象保存到BytesIO中
    image.save(out, 'png')
    # 将BytesIO的文件指针移动到最开始的位置
    out.seek(0)

    response = HttpResponse(content_type='image/png')
    # 从BytesIO的管道中，读取出图片数据，保存到response对象上
    response.write(out.read())
    response['Content-length'] = out.tell()

    # 12Df：12Df.lower()
    cache.set(text.lower(), text.lower(), 5 * 60)

    return response


def check_phone_exist(request):
    '''检测手机号码是否注册'''
    ret = {"status": 0, "msg": ""}
    phone = request.POST.get("phone")
    print(phone)
    is_exist = UserInfo.objects.filter(phone=phone).first()
    print("is_exist:", is_exist)
    if is_exist:
        ret["status"] = 1
        ret["msg"] = "手机号码已被注册！"
    # return JsonResponse(ret)
    return HttpResponse("hello")


def register(request):
    '''用户注册'''
    ret = {"status": 0, "msg": ""}
    if request.method == "POST":
        print("用户注册")
        # print(request.data)
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            username = request.POST.get("username")
            phone = request.POST.get("phone")
            print("this is phone:", phone)
            passwd = request.POST.get("password")
            print("passwd:", passwd)
            form_obj.cleaned_data.pop("re_password")
            avatar_img = request.FILES.get("avatar")

            print("avatar:", avatar_img)
            code = request.POST.get("valid_code")
            print("获取的验证码：", code)
            if code == cache.get(phone):
                print("验证码成功")
                if avatar_img == None:
                    avatar_img="avatars/default.png"
                UserInfo.objects.create_user(**form_obj.cleaned_data, avatar=avatar_img)
                user = auth.authenticate(password=passwd, username=username)
                if user:
                    print("人物创建成功")

                    ret["msg"] = "/userinfo/index/"
                    auth.login(request, user)
                    return JsonResponse(ret)

        else:
            print(form_obj.errors)
            ret["status"] = 1
            ret["msg"] = form_obj.errors
            print(ret)
            print("=" * 120)
            return JsonResponse(ret)

    form_obj = RegForm(request.POST)
    return render(request, "register.html", {"form_obj": form_obj})


def logout(request):
    '''用户退出'''
    auth.logout(request)
    return redirect(reverse('userinfo:index'))
