from django.conf import settings
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
import hashlib
from .models import user
from . import user_decorator
from df_goods.models import *
# Create your views here.
# coding=utf-8
#用户注册
def register(request):
    context = {'title': '用户注册',}
    return render(request, 'df_user/register.html', context)
def register_handle(request):
    #接收用户输入
    post = request.POST
    name = post.get('user_name')
    pwd = post.get('pwd')
    cpwd = post.get('cpwd')
    email = post.get('email')
    #判断两次密码
    if pwd != cpwd:
        return redirect('/tt/register/')
    #密码加密   #from hashlib import  sha1
    pwd2 = hashlib.sha1(b'pwd').hexdigest()
    #创建对象
    user.objects.create(
        name = name,
        pwd = pwd2,
        email = email,
    )
    #注册成功，转到登录
    return redirect('/tt/login/')
#验证用户是否存在
def register_exist(request):
    name = request.GET.get('name')
    count = user.objects.filter(name=name).count()
    return JsonResponse({'count':count})   #JsonResponse返回一个字典
#登录
def login(request):
    name = request.COOKIES.get('name','')
    context = {'title':'用户登录','error_name':'0','error_pwd':'0','user_name':name}
    return render(request, 'df_user/login.html', context)
def login_handle(request):
    ##接收用户输入
    post=request.POST
    name = post.get('name')
    print('name',name)
    pwd = post.get('pwd')
    jizhu = post.get('jizhu',0)
    users = user.objects.filter(name=name)
    print('name:',name)
    print('len:',len(users))
    # print('test:',request.session['name'])
    if len(users) == 1:
        #密码加密
        pwd2 = hashlib.sha1(b'pwd').hexdigest()
        if pwd2 == users[0].pwd:
            # red = HttpResponseRedirect('/tt/index')
            # red = render(request,'index.html')
            url = request.COOKIES.get('url','/tt/index/')#从url取出cookies
            red = HttpResponseRedirect(url)
            if jizhu != 0:
                red.set_cookie('name',name)
            else:
                red.set_cookie('name','',max_age=-1)   #max_age  过期时间
            request.session['user_id']=users[0].id  #user_decorator中
            request.session['user_name']=name
            return  red
        else:
            context = {'title':'用户登录1','error_name':'0','error_pwd':'1','name':name,'pwd':pwd}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title': '用户登录2', 'error_name': '1', 'error_pwd': '0', 'name': name, 'pwd': pwd}
        return render(request, 'df_user/login.html', context)
#退出
def logout(request):
    request.session.flush()
    # user_name = ''
    return render(request,'df_goods/index.html')
#用户信息中心
def user_info(request):
    user_info = user.objects.get(id=request.session['user_id'])
    goods_ids = request.COOKIES.get('goods_ids','')
    print('cook:',goods_ids)
    goods_ids1= goods_ids.split(',')
    goods_list = []
    for goods_id in goods_ids1:
        goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))

    context = {'title':'用户中心',
               'phone':user_info.phone,
               'address':user_info.address,
               'goods_list':goods_list,
               }
    return render(request,'user_center_info.html',context)
#用户定单
# @user_decorator.login
def user_order(request):
    context = {'title':'全部订单',}
    return render(request,'user_center_order.html',context)
#用户收货信息
def user_site(request):
    users = user.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        users.shou = post.get('shou')
        users.address = post.get('address')
        users.zip_code = post.get('zip_code')
        users.phone = post.get('phone')
        users.save()
    context = {'title':'收货地址','users':users,}
    return render(request,'user_center_site.html',context)

#提交订单
def place_order(request):
    users = user.objects.get(id=request.session['user_id'])
    context = {'title':'提交订单',
               'users:':users,
               'address':users.address,
               'shou':users.name,
               'phone':users.phone,
               }
    return render(request,'place_order.html',context)
#全局变量设置
def global_settings(request):
    #全局
    SITE_NAME = settings.SITE_NAME
    # user_name= request.session['name']
    # users = user.objects.get(id=request.session['user_id'])
    return locals()

#test
def test(request):
    return render(request,'test.html',locals())
