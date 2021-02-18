from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url 
from . import views

 

from rest_framework import routers

 


router = routers.DefaultRouter()
router.register(r'customer_profile', views.customersViewSet)
router.register(r'orders', views.ordersViewSet)
router.register(r'product_profile', views.productsViewSet)

 


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url('load/', views.load),
    #url(r'^load/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^load/',views.load),
    path('', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]