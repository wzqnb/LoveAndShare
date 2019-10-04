from django.shortcuts import render, HttpResponse, redirect
from userinfo.models import Article,Category,Tag
from django.db.models import F
from utils.pager import PageInfo
from django.core.cache import cache


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