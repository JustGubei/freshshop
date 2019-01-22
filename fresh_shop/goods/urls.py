"""__author__ =侯晨皓"""

from django.urls import path
from goods import views

urlpatterns = [
    #首页
    path('index/',views.index,name='index'),
    #商品详情
    path('detail/<int:id>/',views.detail,name='detail'),
    #list
    path('list/',views.list,name='list'),
    path('list2/',views.list2,name='list2'),
    path('list3/',views.list3,name='list3'),

    #商品分类查找
    path('list11/',views.list11,name='list11'),
    path('list12/',views.list12,name='list12'),
    path('list13/',views.list13,name='list13'),
    path('list14/',views.list14,name='list14'),
    path('list15/',views.list15,name='list15'),
    path('list16/',views.list16,name='list16'),

]
