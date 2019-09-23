from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from mdeditor.fields import MDTextField
from LoveAndShare import settings

class UserInfo(AbstractUser):
    '''用户信息'''
    phone=models.CharField(verbose_name="电话",max_length=11,unique=True)
    avatar=models.FileField(verbose_name="头像",upload_to="avatars/",default="avatars/default.png")
    create_time=models.DateTimeField(default=datetime.now,verbose_name='创建时间')

    class Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username


class Article(models.Model):
    """文章"""
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )
    COMMENT_STATUS = (
        ('o', '打开'),
        ('c', '关闭'),
    )
    TYPE = (
        ('a', '文章'),
        ('p', '页面'),
    )
    title = models.CharField('标题', max_length=200, unique=True)
    body = MDTextField('正文')
    pub_time = models.DateTimeField('发布时间', blank=False, null=False, default=datetime.now)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES, default='p')
    comment_status = models.CharField('评论状态', max_length=1, choices=COMMENT_STATUS, default='o')
    type = models.CharField('类型', max_length=1, choices=TYPE, default='a')
    views = models.PositiveIntegerField('浏览量', default=0)
    author = models.ForeignKey('UserInfo', verbose_name='作者', blank=False, null=False,
                               on_delete=models.CASCADE)
    article_order = models.IntegerField('排序,数字越大越靠前', blank=False, null=False, default=0)
    category = models.ForeignKey('Category', verbose_name='分类', on_delete=models.CASCADE, blank=False, null=False)
    up_count = models.IntegerField(verbose_name="点赞数", default=0)
    down_count = models.IntegerField(verbose_name="踩数", default=0)
    def body_to_string(self):
        return self.body

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-article_order', '-pub_time']
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        get_latest_by = 'id'

class Category(models.Model):
    """文章分类"""
    name = models.CharField('分类名', max_length=30, unique=True)
    parent_category = models.ForeignKey('self', verbose_name="父级分类", blank=True, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(default='no-slug', max_length=60, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class BlogSettings(models.Model):
        '''站点设置 '''
        sitename = models.CharField("网站名称", max_length=200, null=False, blank=False, default='')
        site_description = models.TextField("网站描述", max_length=1000, null=False, blank=False, default='')
        site_seo_description = models.TextField("网站SEO描述", max_length=1000, null=False, blank=False, default='')
        site_keywords = models.TextField("网站关键字", max_length=1000, null=False, blank=False, default='')
        article_sub_length = models.IntegerField("文章摘要长度", default=300)
        sidebar_article_count = models.IntegerField("侧边栏文章数目", default=10)
        sidebar_comment_count = models.IntegerField("侧边栏评论数目", default=5)
        show_google_adsense = models.BooleanField('是否显示谷歌广告', default=False)
        google_adsense_codes = models.TextField('广告内容', max_length=2000, null=True, blank=True, default='')
        open_site_comment = models.BooleanField('是否打开网站评论功能', default=True)
        beiancode = models.CharField('备案号', max_length=2000, null=True, blank=True, default='')
        analyticscode = models.TextField("网站统计代码", max_length=1000, null=False, blank=False, default='')
        show_gongan_code = models.BooleanField('是否显示公安备案号', default=False, null=False)
        gongan_beiancode = models.TextField('公安备案号', max_length=2000, null=True, blank=True, default='')
        resource_path = models.CharField("静态文件保存地址", max_length=300, null=False, default='/var/www/resource/')

        class Meta:
            verbose_name = '网站配置'
            verbose_name_plural = verbose_name

        def __str__(self):
            return self.sitename


class SideBar(models.Model):
    """侧边栏,可以展示一些html内容"""
    name = models.CharField('标题', max_length=100)
    content = models.TextField("内容")
    sequence = models.IntegerField('排序', unique=True)
    is_enable = models.BooleanField('是否启用', default=True)
    created_time = models.DateTimeField('创建时间', default=datetime.now)
    last_mod_time = models.DateTimeField('修改时间', default=datetime.now)

    class Meta:
        ordering = ['sequence']
        verbose_name = '侧边栏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



