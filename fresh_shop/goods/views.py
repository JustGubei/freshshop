from django.shortcuts import render

from goods.models import GoodsCategory, Goods


def index(request):
    if request.method == 'GET':
        # 如果返回首页，返回渲染的首页index.html页面

        # cate = GoodsCategory.objects.filter().all()
        #
        # gd =Goods.objects.filter().all()


        #[object1,object2,object3,object4,object5,object6]
        #组装结果的对象object：包含分类，该分类的前四个商品信息
        #方式1：object ==> [GoodeCategory Object,[Goods objects1,Goods objects2,Goods objects3,Goods objects4]
        #方式2: object ==> ['category_name':[Goods objects1,Goods objects2,Goods objects3,Goods objects4]
        categorys = GoodsCategory.objects.all()
        good = Goods.objects.all()
        result = []
        for category in categorys:

            goods =  category.goods_set.all()[:4]
            data = [category,goods]
            result.append(data)



        category_type = GoodsCategory.CATEGORY_TYPE



        return render(request,'index.html',
                      {'result':result,'category_type':category_type})


def detail(request,id):
    if request.method == 'GET':
        goods = Goods.objects.filter(pk=id).first()

        #最近浏览

        goods_list = [goods.id,1]
        click = request.session.get('click')

        flag = True
        if click:

            for se_good in click:
                if se_good[0] == goods.id:
                    se_good[1] += 1
                    flag = False
            if flag:
                click.append(goods_list)
                request.session['click'] = click

            return render(request, 'detail.html', {'goods': goods, 'click': click})

        else:
            request.session['click'] = [goods_list]


        return render(request,'detail.html',{'goods':goods,'click':click})

