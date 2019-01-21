from django.http import JsonResponse
from django.shortcuts import render

from cart.models import ShoppingCart
from goods.models import Goods


def add_cart(request):
    if request.method == 'POST':
        #接受商品id值和商品数量num
        #组装存储的商品格式 :{goods_id,num,is_select}
        #组装多个商品格式：[{goods_id,num,is_select},{goods_id,num,is_select},{goods_id,num,is_select},{goods_id,num,is_select}]
        goods_id = int(request.POST.get('goods_id'))
        goods_num = int(request.POST.get('goods_num'))
        goods_list = [goods_id,goods_num,1]



        session_goods = request.session.get('goods')
        if session_goods:
            # 1.添加重复的商品则修改
            # 2.添加的商品不存在于购物车中则新增
            flag = True
            for se_goods in session_goods:
                if se_goods[0] ==goods_id:
                    se_goods[1] += goods_num
                    flag = False
            if flag:
                session_goods.append(goods_list)
            request.session['goods'] = session_goods
            count = len(session_goods)
            return JsonResponse({'code':200,'msg':'请求成功','count':count})

        else:
            #第一次添加购物车，需要组装购物车商品格式为
            ## [{goods_id,num,is_select},{goods_id,num,is_select}]
            request.session['goods'] = [goods_list]
            count = 1

        return JsonResponse({'code': 200, 'msg': '请求成功', 'count': count})


def cart_num(request):
    if request.method == 'GET':
        session_goods = request.session.get('goods')
        count = len(session_goods) if session_goods else 0

        return JsonResponse({'code':200,'msg':'请求成功','count':count})


def cart(request):
    if request.method == 'GET':
        session_goods =  request.session.get('goods')
        #组装返回格式 [objects1,objects2]
        # objects ==> Goods Object, is select ,num , total_price
        result = []
        if session_goods:
            for se_goods in session_goods:
                data = []
                #[{goods_id, num, is_select}]
                goods = Goods.objects.filter(pk=se_goods[0]).first()
                total_price = goods.shop_price * se_goods[1]
                data = [goods,se_goods[1],se_goods[2],total_price]
                result.append(data)


        return render(request,'cart.html',{'result':result})


def cart_price(request):
    if request.method == 'GET':
        session_goods = request.session.get('goods')
        all_total = len(session_goods) if session_goods else 0
        all_price = 0
        is_select_num = 0

        for se_goods in session_goods:
            #{goods_id, num, is_select}]
            if se_goods[2]:
                goods =  Goods.objects.filter(pk=se_goods[0]).first()
                all_price += goods.shop_price * se_goods[1]
                is_select_num += 1



        return JsonResponse({'code': 200,
                             'msg':'请求成功',
                             'all_price':all_price,
                             'all_total':all_total,
                             'is_select_num':is_select_num
                             })


def change_cart(request):
    if request.method == 'POST':

        #修改商品的数量和选择状态
        #其实就是修改session中商品信息，结构为 {goods_id, num, is_select}]

        #1.获取商品id值  和  数量/选择状态

        goods_id = int(request.POST.get('goods_id'))
        goods_num = request.POST.get('goods_num')
        goods_select = request.POST.get('goods_selcet')

        #修改


        session_goods = request.session.get('goods')

        for se_goods in session_goods:
            if se_goods[0] == goods_id:
                se_goods[1] = int(goods_num) if goods_num else se_goods[1]
                se_goods[2] = int(goods_select) if goods_select else se_goods[2]

        request.session['goods'] = session_goods


        return JsonResponse({'code':200,'msg':'请求成功'})



def del_cart(request):
    if request.method == 'POST':

        # 删除购物车中的商品
        # 其实就是删除session中商品信息，结构为 {goods_id, num, is_select}

        goods_id = int(request.POST.get('goods_id'))

        session_goods = request.session.get('goods')


        #下标删除
        if len(session_goods)>1:

            for index in range(len(session_goods)-1):
                if session_goods[index][0] == goods_id:
                    del session_goods[index]
        else:
            del session_goods[0]

        request.session['goods'] = session_goods

        user_id = request.session.get('user_id')
        #删除数据库中购物车中的商品信息
        if user_id:

            ShoppingCart.objects.filter(user_id=user_id,goods_id=goods_id).delete()

        return JsonResponse({'code':200,'msg':'删除成功'})


#修改选择状态

def change_cart1(request):
    if request.method == 'POST':

        #修改商品的数量和选择状态
        #其实就是修改session中商品信息，结构为 {goods_id, num, is_select}]

        #1.获取商品id值  和  数量/选择状态

        goods_id = int(request.POST.get('goods_id'))
        goods_num = request.POST.get('goods_num')
        goods_select = request.POST.get('goods_select')
        select = 0
        if int(goods_select)== 1:
            select = 0
        else:
            select = 1
        #修改


        session_goods = request.session.get('goods')

        for se_goods in session_goods:
            if se_goods[0] == goods_id:
                se_goods[2] = select

        request.session['goods'] = session_goods


        return JsonResponse({'code':200,'msg':'请求成功'})



def del_cart2(request,id):
    if request.method == 'POST':
        #思路通过传入的商品id值，去session中查找，查找到则删除数据

        session_goods = request.session.get('goods')

        for se_goods in session_goods:
            # se_goods结构为{goods_id, num, is_select}]
            # print(se_goods[0], id)
            if se_goods[0] == id:
                session_goods.remove(se_goods)
                break

        request.session['goods'] = session_goods

        user_id = request.session.get('user_id')

        if user_id:

            ShoppingCart.objects.filter(user_id=user_id,goods_id=id).delete()

        return JsonResponse({'code':200,'msg':'删除成功'})

