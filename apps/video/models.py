from django.db import models

# Create your models here.

#encoding: utf-8

from django.db import models


class CourseCategory(models.Model):
    name = models.CharField(max_length=100,verbose_name="视频分类")
    class Meta:
        verbose_name = '视频分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200,verbose_name="资料名称")
    category = models.ForeignKey('CourseCategory',on_delete=models.DO_NOTHING)
    img= models.FileField(verbose_name="图片", upload_to="video_img/", default="")
    profile = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '视频名称'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Vidoe(models.Model):
    title = models.CharField(max_length=200, verbose_name="视频")
    course = models.ForeignKey('Course', on_delete=models.DO_NOTHING)
    profile = models.TextField()
    video_url = models.URLField()
    cover_url = models.URLField()
    pub_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title