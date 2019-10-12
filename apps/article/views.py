from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect,reverse
from userinfo.models import *
from django.db.models import F
from utils.pager import PageInfo
from LoveAndShare import settings
import os
from bs4 import BeautifulSoup
import html
from bleach.sanitizer import ALLOWED_ATTRIBUTES, ALLOWED_TAGS
from django.views.decorators.cache import cache_page
import bleach
from notifications.signals import notify


from django.core.cache import cache
import json


# Create your views here.

def article_detail(request, id):
    '''文章详情'''
    article = Article.objects.filter(id=id).first()
    Article.objects.filter(id=id).update(views=F("views") + 1)
    comment_list = Comment.objects.filter(article_id=id)
    if article:
        return render(request, "article/article_detail.html", {"article": article, "comment_list": comment_list})
    else:
        return HttpResponse("404")

@cache_page(60*60*24)
def article_category(request, category):
    '''文章分类'''
    category_obj = Category.objects.filter(name=category).first()
    category_article = category_obj.article_set.all()

    return render(request, "article/article_list.html", {"article_list": category_article})

@cache_page(60*60*24)
def article_tag(request, tag):
    '''文章标签'''
    tag = Tag.objects.filter(title=tag).first()
    tag_article = tag.article_set.all()
    return render(request, "article/article_list.html", {"article_list": tag_article})

@cache_page(60*60*24)
def article_archive(request):
    '''文章归档'''
    article_list = Article.objects.all().order_by("-pub_time")

    return render(request, "article/article_archive.html", {"article_list": article_list})


def article_updown(request):
    '''文章点赞或不喜欢'''
    article_id = request.POST.get("article_id")
    article=Article.objects.filter(id=article_id)
    is_up = json.loads(request.POST.get('is_up'))
    user = request.user
    response = {"state": True}
    article_obj = Article.objects.filter(id=article_id).first()
    article_obj = article_obj.author.username
    try:
        ArticleUpDown.objects.create(user=user, article_id=article_id, is_up=is_up)
        if is_up:
            Article.objects.filter(pk=article_id).update(up_count=F("up_count") + 1)
            notify.send(
                request.user,
                recipient=article_obj,
                verb='回复了你',
                target=article,
                # action_object=new_comment,
            )
        else:
            Article.objects.filter(pk=article_id).update(down_count=F("down_count") + 1)
        # user与articlie_id已经做了联合唯一索引 第一次点赞或踩都进行操作
        # 但第二次不论点还是踩 都会报错因为已经联合唯一了

    except Exception as e:
        response["state"] = False
        response["fisrt_action"] = ArticleUpDown.objects.filter(user=user, article_id=article_id).first().is_up
        # 把点赞还是踩的状态拿出来
    return JsonResponse(response)


def comment(request):
    import html
    '''文章评论'''
    # pid判断是子评论还是父评论
    pid = request.POST.get("pid")
    article_id = request.POST.get("article_id")
    article = Article.objects.filter(id=article_id).first()
    content = request.POST.get("content")
    content = html.escape(content, quote=True)
    user_pk = request.user.pk
    response = {}
    article_obj = Article.objects.filter(id=article_id).first()
    article_obj = UserInfo.objects.filter(id=article_obj.author.id).first()
    if not pid:
        # 父评论

        notify.send(
            request.user,
            recipient=article_obj,
            verb='回复了你',
            target=article,
            # action_object=new_comment,
        )
        comment_obj = Comment.objects.create(article_id=article_id, user_id=user_pk, content=content)
        Article.objects.filter(pk=article_id).update(comment_count=F("comment_count") + 1)
    else:
        # 子评论
        notify.send(
            request.user,
            recipient=article_obj,
            verb='回复了你',
            target=article,
            # action_object=new_comment,
        )
        comment_obj = Comment.objects.create(article_id=article_id, user_id=user_pk, content=content,
                                             parent_comment_id=pid)
        Article.objects.filter(pk=article_id).update(comment_count=F("comment_count") + 1)


    response["create_time"] = comment_obj.create_time.strftime("%Y-%m-%d")
    response["content"] = comment_obj.content
    response["username"] = comment_obj.user.username
    return JsonResponse(response)




def article_add(request):
    '''文章添加'''
    if request.method == "POST":
        c = request.POST
        c = dict(c)
        tag = c['tag']
        title = request.POST.get("title")
        category = request.POST.get("category")
        article_content = request.POST.get('article_content')

        bs = BeautifulSoup(article_content, "html.parser")
        desc = bs.text[0:150] + "..."
        tags = ALLOWED_TAGS + ['img', 'h1', 'h2', 'h3', 'h4', 'h5', 'sup', 'big', 'small', 'p', 'span', 'br',
                               'dfn', 'div', 'cite', 'font', 'strike', 'sub', 'tt', 'u', 'pre']
        attributes = {**ALLOWED_ATTRIBUTES, 'img': ['src']}
        cleaned_content = bleach.clean(article_content, tags=tags, attributes=attributes)
        category_id = Category.objects.filter(name=category).first().pk
        article = Article.objects.create(title=title, desc=desc, body=cleaned_content, author_id=request.user.pk,
                                         category_id=category_id)
        article_pk = article.pk

        for title in tag:
            id = Tag.objects.filter(title=title).first().pk
            print(id, title)
            Article2Tag.objects.create(article_id=article_pk, tag_id=id)

    category_list = Category.objects.all()
    tags_list = Tag.objects.all()
    return render(request, "article/add_article.html", {"category_list": category_list, "tags_list": tags_list})


def article_image_upload(request):
    '''图片上传'''
    obj = request.FILES.get("upload_img")
    path = os.path.join(settings.MEDIA_ROOT, "article_img", obj.name)
    with open(path, "wb") as f:
        for line in obj:
            f.write(line)

    res = {
        "error": 0,
        "url": "/media/article_img/" + obj.name
    }

    return JsonResponse(res)


def article_list_forme(request, pk):
    '''个人文章列表'''
    article_list = Article.objects.filter(author_id=pk)
    return render(request, "article/article_list_forme.html", {"article_list": article_list})


def article_detele(request):
    '''文章删除'''
    id = request.POST.get("id")
    Article.objects.filter(id=id).delete()
    return JsonResponse({})


def article_editor(request, id):
    '''文章修改'''
    print(request.path)
    article = Article.objects.filter(id=id).first()
    category_list = Category.objects.all()
    tags_list = Tag.objects.all()
    editor = True
    return render(request, "article/editor_article.html",
                  {"article": article, editor: "editor", "category_list": category_list, "tags_list": tags_list})


def article_editor_save(request):
    "文章修改保存 直接把原来的文章删除 重新创建文章"
    url=request.get_full_path()
    url=url.split("=")
    id=url[1]
    Article.objects.filter(id=id).delete()

    c = request.POST
    c = dict(c)
    tag = c['tag']
    title = request.POST.get("title")
    category = request.POST.get("category")
    article_content = request.POST.get('article_content')

    bs = BeautifulSoup(article_content, "html.parser")
    desc = bs.text[0:150] + "..."
    tags = ALLOWED_TAGS + ['img', 'h1', 'h2', 'h3', 'h4', 'h5', 'sup', 'big', 'small', 'p', 'span', 'br',
                           'dfn', 'div', 'cite', 'font', 'strike', 'sub', 'tt', 'u', 'pre']
    attributes = {**ALLOWED_ATTRIBUTES, 'img': ['src']}
    cleaned_content = bleach.clean(article_content, tags=tags, attributes=attributes)
    category_id = Category.objects.filter(name=category).first().pk
    article = Article.objects.create(title=title, desc=desc, body=cleaned_content, author_id=request.user.pk,
                                    category_id=category_id)
    article_pk = article.pk

    for title in tag:
        id = Tag.objects.filter(title=title).first().pk
        print(id, title)
        Article2Tag.objects.create(article_id=article_pk, tag_id=id)

    return redirect(reverse("article/article:article_list_forme",args=(request.user.pk,)))


