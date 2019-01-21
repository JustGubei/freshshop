"""__author__ =侯晨皓"""
from django.urls import path
from order import views

urlpatterns = [
    #结算功能
    path('place_order/',views.place_order,name='place_order'),
    #创建订单
    path('order/',views.order,name='order'),
    #全部订单
    path('user_order/',views.user_order,name='user_order'),


]


