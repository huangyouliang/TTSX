from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, redirect
from .models import GoodsInfo,TypeInfo,CartInfo
from df_userInfo.models import user
# Create your views here.
#主页
def index(request):
    typelist = TypeInfo.objects.all()
    best_new0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]#查出4条最新的
    best_sell0=typelist[0].goodsinfo_set.order_by('-gclick')[0:4]#查出4条最热的
    best_new1= typelist[1].goodsinfo_set.order_by('-id')[0:4]
    best_sell1 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    best_new2= typelist[2].goodsinfo_set.order_by('-id')[0:4]
    best_sell2 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    best_new3= typelist[3].goodsinfo_set.order_by('-id')[0:4]
    best_sell3 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    best_new4= typelist[4].goodsinfo_set.order_by('-id')[0:4]
    best_sell4 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    best_new5= typelist[5].goodsinfo_set.order_by('-id')[0:4]
    best_sell5 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]

    context = {'title':'主页',
               'best_new0':best_new0, 'best_new1': best_new1,
               'best_new2': best_new2, 'best_new3': best_new3,
               'best_new4': best_new4, 'best_new5': best_new5,
               'best_sell0':best_sell0, 'best_sell11': best_sell1,
               'best_sell2': best_sell2,'best_sell3': best_sell3,
               'best_sell4': best_sell4, 'best_sell5': best_sell5,
               }
    return render(request, 'df_goods/index.html', context)

#商品详细信息
def detail(request,id):
    goods = GoodsInfo.objects.get(pk=int(id))
    goods.gclick = goods.gclick+1
    goods.save()
    news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {
        'title':'商品详细信息',
         'user_name':request.session['user_name'],
        'g':goods,
        'news_goods':news,
    }
    response=render(request,'df_goods/detail.html',context)

    #good_ids
    goods_ids = request.COOKIES.get('goods_ids','')  #保存good_ids cookies
    goods_id = '%d'%goods.id   #以字符串的形式展示goods.id    int----字符串
    if goods_ids != '':
        goods_ids1 = goods_ids.split(',')    #分割  拆分为列表
        if goods_ids1.count(goods_id)>=1:   #保证只有一个goods_ids1
            goods_ids1.remove(goods_id)
        goods_ids1.insert(0,goods_id) #插入goods_id  到 goods_ids1
        if len(goods_ids1)>=6:   #要求只要前五个
            del goods_ids1[5]
        goods_ids = ','.join(goods_ids1)  #id 以‘，’j加入到goods_ids   拼接为字符串
    else:
        goods_ids = goods_id #没有记录直接添加
    response.set_cookie('goods_ids',goods_ids)  #goods_ids写入到cookie
    return response


#分类列表
def list(request,tid,pindex,sort):
    typeinfo =TypeInfo.objects.get(pk=int(tid))
    news=typeinfo.goodsinfo_set.order_by('-id')[0:2]
    if sort == '1':#默认，最新排序
        # goods_list = typeinfo.goodsinfo_set.order_by('-id')
        goods_list = GoodsInfo.objects.filter(gtype=int(tid)).order_by('id')
    elif sort ==  '2': #价格
        # goods_list = typeinfo.goodsinfo_set.order_by('-gprice')
        goods_list = GoodsInfo.objects.filter(gtype=tid).order_by('gprice')
    elif sort == '3':#人气
        # goods_list = typeinfo.goodsinfo_set.order_by('gclick')
        goods_list = GoodsInfo.objects.filter(gtype=tid).order_by('gclick')
    paginator = Paginator(goods_list,5)  #Paginator(goods_list,num)   num 指每页显示的条目
    page = paginator.page(int(pindex))   #Paginator.page(number) 返回指定页的对象
    print('tid:',tid)
    context = {
        'title':'商品列表',
        'tid':tid,
        'typeinfo':typeinfo,
        'new_goods':news,
        'goods_list':goods_list,
        'paginator':paginator,
        'page':page,
        'sort':sort,
    }
    return render(request, 'df_goods/list.html', context)
#购物车
def cart(request):
    uid = request.session['user_id']
    cart_list = CartInfo.objects.filter(user_id = uid)
    # aq=CartInfo.objects.filter(user_id=uid).count(number)
    # print('num:',aq)
    context = {'title': '我的购物车',
               'cart_list':cart_list,
               # 'sum':sum1,
               }
    return render(request, 'df_goods/cart.html', context)
#添加到购物车
def add(request,gid,count):
    gid = int(gid)
    count = int(count)
    uid = request.session['user_id']
    print('a:',gid)
    cart = CartInfo.objects.filter(user_id=uid,good_id=gid)
    print('len:', len(cart))
    if len(cart)>=1:
        cart=cart[0]   #取第一条商品的名称
        cart.number = cart.number+count
    else:
        cart=CartInfo()
        cart.user_id = uid
        cart.good_id = gid
        cart.number = count
    cart.save()
    return redirect('/tt/cart/')

#删除
def delete(request,gid):
    gid = int(gid)
    CartInfo.objects.get(good_id=gid).delete()
    return  redirect('/tt/cart/')
#增加数量
def add_num(request,gid,num):
    num = int(num)
    CartInfo.objects.filter(good_id=gid).update(number=num+1)
    return  redirect('/tt/cart/')
#减少数量
def min_num(request,gid,num):
    num = int(num)
    CartInfo.objects.filter(good_id=gid).update(number=num - 1)
    return  redirect('/tt/cart/')
