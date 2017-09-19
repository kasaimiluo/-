# -*- coding:utf-8 -*-
from django.db import models

# Create your models here..
class UserMessage(models.Model):
    #object_id=models.CharField(max_length=50,default="",primary_key=True,verbose_name="主键")
    name=models.CharField(max_length=20,primary_key=True,default="",verbose_name="用户名")
    sex=models.CharField(max_length=10,null=True,blank=True,default="",verbose_name="性别")
    age = models.CharField( max_length=30, null=True, blank=True, default="", verbose_name="年龄")
    university = models.CharField(max_length=30, null=True, blank=True, default="", verbose_name="所在高校")
    major = models.CharField(max_length=40, null=True, blank=True, default="", verbose_name="所读专业")
    email=models.EmailField(verbose_name=u"邮箱")
    address=models.CharField(max_length=100,verbose_name=u"联系地址")
    message=models.CharField(max_length=500,verbose_name=u"留言信息")

    class Meta:
        verbose_name=u"用户留言信息"
        verbose_name_plural=verbose_name
