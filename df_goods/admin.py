# -*-coding:utf-8 -*-
from django.contrib import admin
from .models import *
# Register your models here.
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ('gtitle','gclick','gkucun','gprice','gtype')
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ('ttitle')
admin.site.register(GoodsInfo,GoodsInfoAdmin)
admin.site.register(TypeInfo)