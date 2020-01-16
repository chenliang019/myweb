from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.index),
    re_path('(?P<year>[0-9]{4}).html',views.myyear,name='myyear'),
    path('download.html',views.download),
    path('index.html',views.huawei),
    path('login.html',views.login),
    path('test.html',views.test)
]