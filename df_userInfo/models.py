from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-

#创建用户
class user(models.Model):
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=40)
    email = models.EmailField(max_length=30)
    shou = models.CharField(max_length=20,default = '')
    address = models.CharField(max_length=100,default = '')
    zip_code= models.CharField(max_length=6,default = '')
    phone = models.CharField(max_length=11,default = '')
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
        def __unicode__(self):
            return self.name.encode('utf-8')

