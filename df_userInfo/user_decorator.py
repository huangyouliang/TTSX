#coding-utf-8
from django.http import HttpResponseRedirect
def login(func):
    def login_fun(request,*args,**kwargs):#url 之外的参数的兼容*args  **kwargs
        if request.session.has_key('name'):#session 判断
            return func(request,*args,**kwargs)
        else:
            red = HttpResponseRedirect('/tt/login/')
            red.set_cookie('url',request.get_full_path())#request.get_path  request.get_full_path()  完全路径（带参数）
            return red
    return login_fun