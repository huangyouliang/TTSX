from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^register/',views.register),
    url(r'^register_handle',views.register_handle),
    url(r'^register_exist',views.register_exist),
    url(r'^login/',views.login),
    url(r'^logout',views.logout),
    url(r'^login_handle/',views.login_handle),
    url(r'^user_info/',views.user_info),
    url(r'^user_order/', views.user_order, name='user_center_order'),
    url(r'^user_site/', views.user_site),
    url(r'^place_order/',views.place_order),
    url(r'^test/',views.test,name='test'),

]