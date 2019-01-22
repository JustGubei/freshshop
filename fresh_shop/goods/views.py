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

        goods.click_nums = goods.click_nums + 1
        goods.is_hot = goods.is_hot + 1
        goods.save()
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




def list(request):
    if request.method == 'GET':
        new_goods = Goods.objects.order_by('-id')[:5]
        goods = Goods.objects.all()
        return render(request,'list.html',{'goods':goods,'new_goods':new_goods})


def list2(request):
    if request.method == 'GET':
        new_goods = Goods.objects.order_by('-id')[:5]
        goods = Goods.objects.order_by('shop_price')
        return render(request,'list.html',{'goods':goods,'new_goods':new_goods})



def list3(request):
    if request.method == 'GET':
        new_goods = Goods.objects.order_by('-id')[:5]
        goods = Goods.objects.order_by('is_hot')
        return render(request,'list.html',{'goods':goods,'new_goods':new_goods})


def list11(request):
    if request.method == 'GET':
        new_goods = Goods.objects.order_by('-id')[:5]
        goods = Goods.objects.filter(category_id=1)
        return render(request,'list.html',{'goods':goods,'new_goods':new_goods})

def list12(request):
    if request.method == 'GET':
        new_goods = Goods.objects.order_by('-id')[:5]
        goods = Goods.objects.filter(category_id=2)
        return render(request,'list.html',{'goods':goods,'new_goods':new_goods})
def list13(request):
    if request.method == 'GET':
        new_goods = Goods.objects.order_by('-id')[:5]
        goods = Goods.objects.filter(category_id=3)
        return render(request,'list.html',{'goods':goods,'new_goods':new_goods})

def list14(request):
    if request.method == 'GET':
        new_goods = Goods.objects.order_by('-id')[:5]
        goods = Goods.objects.filter(category_id=4)
        return render(request,'list.html',{'goods':goods,'new_goods':new_goods})

def list15(request):
    if request.method == 'GET':
        new_goods = Goods.objects.order_by('-id')[:5]
        goods = Goods.objects.filter(category_id=5)
        return render(request,'list.html',{'goods':goods,'new_goods':new_goods})

def list16(request):
    if request.method == 'GET':
        new_goods = Goods.objects.order_by('-id')[:5]
        goods = Goods.objects.filter(category_id=6)
        return render(request,'list.html',{'goods':goods,'new_goods':new_goods})

