"""__author__ =侯晨皓"""

from django.urls import path
from goods import views

urlpatterns = [
    #首页
    path('index/',views.index,name='index'),
    #商品详情
    path('detail/<int:id>/',views.detail,name='detail'),

]
