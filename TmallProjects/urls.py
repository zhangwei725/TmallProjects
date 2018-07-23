from django.conf.urls import url
from django.contrib import admin
import xadmin

urlpatterns = [
    # url('admin/', admin.site.urls),
    # 替换admin为xadmin
    url('xadmin/', xadmin.site.urls)
]
