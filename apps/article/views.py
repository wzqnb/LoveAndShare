from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from userinfo.models import Article,Category,Tag,ArticleUpDown
from django.db.models import F
from utils.pager import PageInfo
from django.core.cache import cache
import json


# Create your views here.

def article_detail(request, id):
    '''文章详情'''
    article = Article.objects.filter(id=id).first()
    Article.objects.filter(id=id).update(views=F("views") + 1)
    print(article)
    if article:
        return render(request, "article_detail.html", {"article": article})
    else:
        return HttpResponse("404")

def article_category(request,category):
    '''文章分类'''
    category_obj=Category.objects.filter(name=category).first()
    count=category_obj.article_set.all().count()
    page_info = PageInfo(request.GET.get('page'), count, 2, '/article/article_category/category', 11)
    category_article = category_obj.article_set.all()[page_info.start():page_info.end()]

    return render(request, "article_list.html", {"article_list": category_article,"page_info":page_info})


def article_tag(request,tag):
    '''文章标签'''
    tag = Tag.objects.filter(title=tag).first()
    print(tag)
    tag_article= tag.article_set.all()
    return render(request,"article_list.html",{"article_list":tag_article})


def article_archive(request):
    '''文章归档'''
    article_list=Article.objects.all().order_by("-pub_time")


    return render(request,"article_archive.html",{"article_list":article_list})

def article_updown(request):
    '''文章点赞或不喜欢'''
    article_id = request.POST.get("article_id")
    print("article_id",article_id)

    is_up = json.loads(request.POST.get('is_up'))
    print("is_up",is_up)
    user = request.user
    response = {"state": True}
    try:
        ArticleUpDown.objects.create(user=user, article_id=article_id, is_up=is_up)
        if is_up:
            print("dianzan",is_up)
            Article.objects.filter(pk=article_id).update(up_count=F("up_count") + 1)
        # user与articlie_id已经做了联合唯一索引 第一次点赞或踩都进行操作
        else:
            print("vuxihaun", is_up)
            Article.objects.filter(pk=article_id).update(down_count=F("down_count") + 1)
        # 但第二次不论点还是踩 都会报错因为已经联合唯一了

    except Exception as e:
        response["state"] = False
        response["fisrt_action"] = ArticleUpDown.objects.filter(user=user, article_id=article_id).first().is_up
        # 把点赞还是踩的状态拿出来
    return JsonResponse(response)

