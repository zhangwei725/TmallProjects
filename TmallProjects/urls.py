from django.conf.urls import url, include
from django.contrib import admin
import xadmin

from apps.home import views

urlpatterns = [
    # url('admin/', admin.site.urls),
    # 替换admin为xadmin
    url('xadmin/', xadmin.site.urls),
    url('^$', views.index, name='index'),
    url('home/', include('apps.home.urls'))
]
