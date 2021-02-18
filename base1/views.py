from django.shortcuts import render
from django.http import HttpResponse
from base1.helper import *

 

from rest_framework import viewsets
from .serializers import *

 


def load(request):
   populate_products()
   populate_orders(10)
   return HttpResponse('loading completed')

 


class customersViewSet(viewsets.ModelViewSet):
    queryset = customers.objects.all().order_by('c_id')
    serializer_class = customers_serializer

 


class ordersViewSet(viewsets.ModelViewSet):
    queryset = orders.objects.all().order_by('order_id')
    serializer_class = orders_serializer

 


class productsViewSet(viewsets.ModelViewSet):
    queryset = products.objects.all().order_by('product_id')
    serializer_class = products_serializer