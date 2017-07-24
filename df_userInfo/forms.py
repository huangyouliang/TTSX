from  django import forms
# -*- coding: utf-8 -*-
from .models import *
class  UserInfo(forms.Form):
    name = forms.CharField(max_length=20)
    pwd = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=30)
    shou = forms.CharField(max_length=20)
    address = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=6)
    phone = forms.CharField(max_length=11)



class deliver_addressForm(forms.Form):
    deliver = forms.CharField(label='收件人', max_length=20)
    deliver_address_detail = forms.CharField(label='详细地址', max_length=50)
    phone = forms.CharField(label='联系电话', max_length=11)
    zip_code = forms.CharField(label='邮编', max_length=20)
