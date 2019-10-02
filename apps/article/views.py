from django.shortcuts import render, HttpResponse, redirect
from userinfo.models import Article
from django.db.models import F


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

# def article_category(request):
#     pass
#
# def article_tag(request):
#     pass
