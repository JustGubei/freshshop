"""__author__ =侯晨皓"""
from django.urls import path
from cart import views
urlpatterns = [
    #加入购物车
    path('add_cart/',views.add_cart,name='add_cart'),
    #购物车数量刷新
    path('cart_num/',views.cart_num,name='cart_num'),
    #购物车
    path('cart/',views.cart,name='cart'),
    #购物车计算价格
    path('cart_price/',views.cart_price,name='cart_price'),
    #修改购物车中商品的数量  /
    path('change_cart/',views.change_cart,name='change_cart'),
    #修改选择状态
    path('change_cart1/',views.change_cart1,name='change_cart1'),
    #删除购物车中的商品
    path('del_cart/',views.del_cart,name='del_cart'),
    #删除2
    path('del_cart2/<int:id>/',views.del_cart2,name='del_cart2'),
]


