from django.shortcuts import render

# Create your views here.
from apps.home.models import Navigation, Category, Banner


def index(request):
    navigations = Navigation.objects.all()
    # 获取分类菜单的数据
    categories = Category.objects.all()
    for category in categories:
        category.subs = category.submenu_set.all()
        # 获取分类二级菜单的数据
        for sub in category.subs:
            # 获取分类二级菜单的子数据
            sub.subs2 = sub.submenu2_set.all()
        #    ======== 结束======
        category.shops = category.shop_set.all()[0:5]

        # 获取商品的图片
        for shop in category.shops:
            shop.img = shop.shopimage_set.filter(type='type_single').order_by('shop_img_id').first()

    # 获取轮播图数据
    banners = Banner.objects.all().order_by('banner_id')

    return render(request, 'index.html', {'navigations': navigations,
                                          'banners': banners,
                                          'categories': categories})
