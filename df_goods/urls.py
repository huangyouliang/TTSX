from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^index/',views.index),
    url(r'^(\d+)/$',views.detail),
    url(r'^list(\d+)_(\d+)_(\d+)/$',views.list),
    url(r'^cart/',views.cart),
    url(r'^add(\d+)_(\d+)/$',views.add),
    url(r'^del(\d+)/$',views.delete),
    url(r'^add_num(\d+)_(\d+)/',views.add_num),
    url(r'^min_num(\d+)_(\d+)/',views.min_num),
]