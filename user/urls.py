from django.urls import path
from .views import *
urlpatterns=[
    #用户注册和登录
    path('login.html', loginView, name='login'),
    #用户中心
    path('home/<int:page>.html', homeView, name='home'),
    #退出用户登录
    path('logout.html', logoutView,name='logout'),
]