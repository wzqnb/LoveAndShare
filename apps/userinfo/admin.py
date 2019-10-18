from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(UserInfo)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article2Tag)
admin.site.register(Collect)