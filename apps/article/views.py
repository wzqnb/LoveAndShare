from django.shortcuts import render,HttpResponse,redirect
from userinfo.models import Article

# Create your views here.

def article_detail(request,id):
    print(id)
    article=Article.objects.filter(id=id).first()
    print(article)
    if article:
        return render(request,"article_detail.html",{"article":article})
    else:
        return HttpResponse("404")




