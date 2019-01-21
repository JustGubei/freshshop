from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from goods.models import Goods
from user.froms import RegisterForm, LoginForm, AddressForm
from user.models import User, UserAddress


def register(requeset):
    if requeset.method == 'GET':
        return render(requeset,'register.html')
    if requeset.method == 'POST':

        form = RegisterForm(requeset.POST)
        if form.is_valid():
            username = form.cleaned_data.get('user_name')
            password = make_password(form.cleaned_data.get('pwd'))
            email = form.cleaned_data.get('email')



            User.objects.create(username=username,
                                password=password,
                                email=email)

            #账号不存在于数据库，密码和确认密码一致，邮箱格式正确
            return HttpResponseRedirect(reverse('user:login'))
        else:
            errors = form.errors
            return render(requeset, 'register.html', {'errors': errors})


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.filter(username=username).first()
            request.session['user_id'] = user.id

            return  HttpResponseRedirect(reverse('goods:index'))

        else:
            errors = form.errors
            return render(request,'login.html',{'errors':errors})

def logout(request):
    if request.method == 'GET':
        #删掉session中的键值对
        del request.session['user_id']
        #删除session
        del request.session['click']
        # 删除商品信息
        if request.session.get('goods'):

            del request.session['goods']



        return HttpResponseRedirect(reverse('goods:index'))




def user_site(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        user_address = UserAddress.objects.filter(user_id=user_id)

        activate = 'site'
        return render(request,'user_center_site.html',{'user_address':user_address,'activate':activate})

    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            address = form.cleaned_data.get('address')
            postcode = form.cleaned_data.get('postcode')
            mobile = form.cleaned_data.get('mobile')
            user_id = request.session.get('user_id')

            UserAddress.objects.create(user_id=user_id,
                                       address=address,
                                       signer_name=username,
                                       signer_mobile=mobile,
                                       signer_postcode=postcode)

            return HttpResponseRedirect(reverse('user:user_site'))


        else:
            errors = form.errors
            return render(request,'user_center_site.html',{'errors':errors})


        pass


def user_info(request):
    if request.method == 'GET':

        user_id = request.session.get('user_id')
        user_address = UserAddress.objects.filter(user_id=user_id)
        activate = 'info'

        goods_id = request.session.get('goods_id')

        click = request.session.get('click')
        goods_list = []
        if click:
            for se_good in click:
                goods = Goods.objects.filter(pk=se_good[0]).first()
                goods_list.append(goods)


        return render(request,'user_center_info.html',{'user_address':user_address,'activate':activate,'goods_list':goods_list})


