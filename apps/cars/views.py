from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.home.models import ShopCar, Shop


@login_required
def add_car(request):
    try:
        # 查询主表   就直接能获取子表的数据
        # 查询子表   也可以直接子表.外键
        uid = request.user.userprofile.uid
        num = int(request.GET.get('num'))
        shop_id = int(request.GET.get('shop_id'))
        # 两个操作
        # 创建操作 如果商品不存在购物车
        # 更新的操作  商品已经存在   数量+
        car = ShopCar.objects.filter(user=request.user.userprofile, shop_id=shop_id)
        if car:
            # 更新  数字 + 数字  运算
            car = car.first()
            car.number += num
            car.save()
        else:
            car = ShopCar(user_id=uid, shop_id=shop_id, number=num)
            car.save()
            request.session['count'] += 1
        return HttpResponse('success')
    except Exception as e:
        return HttpResponse('error')


# 商品的图片  商品的名称  商品的价格   商品的数量
# values
@login_required
def show(request):
    cars = ShopCar.objects.filter(user_id=request.user.userprofile.uid)
    for car in cars:
        # 获取 商品的图片信息
        car.img = car.shop.shopimage_set.all().first()
    return render(request, 'cars.html', {'cars': cars})
