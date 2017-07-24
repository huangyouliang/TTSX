from django.db import models
from tinymce.models import HTMLField
from df_userInfo.models import *
# Create your models here.
class TypeInfo(models.Model):
    ttitle = models.CharField('商品分类',max_length=20)
    isDelete = models.BooleanField('是否删除',default=False)

    def __str__(self):
        return str(self.ttitle)
    class Meta:
        verbose_name = '列表信息'
        verbose_name_plural = verbose_name
        def __unicode__(self):
            return self.ttitle.encode('utf-8')

class GoodsInfo(models.Model):
    gtitle = models.CharField('商品名称',max_length=20)
    gpic =models.ImageField('商品照片',upload_to='goods')
    gprice =models.DecimalField('商品价格',max_digits=5,decimal_places=2)
    isDelete =models.BooleanField('是否删除',default=False)
    gunit =models.CharField('商品重量',max_length=20,default='500g')
    gclick =models.IntegerField('点击量',)
    gjianjie =models.CharField('简介',max_length=200)
    gkucun = models.IntegerField('库存',)
    gcontent = HTMLField('详细信息')
    gtype = models.ForeignKey(TypeInfo)
    # gadv = models.BooleanField('广告',default=False)
    def __str__(self):
        return str(self.gtitle)

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name
        def __unicode__(self):
            return self.gtitle.encode('utf-8')

#购物车
class CartInfo(models.Model):
    user = models.ForeignKey('df_userInfo.user')
    good = models.ForeignKey('df_goods.GoodsInfo')
    number = models.IntegerField('数量')

