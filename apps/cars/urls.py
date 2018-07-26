from django.conf.urls import url

from apps.cars import views

urlpatterns = [
    url('add/', views.add_car, name='add_car'),
    url('show/', views.show, name='show')
]
