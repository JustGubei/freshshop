"""__author__ =侯晨皓"""
from django.urls import path
from user import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    #地址
    path('user_site/',views.user_site,name='user_site'),
    #用户
    path('user_info/',views.user_info,name='user_info'),



]
