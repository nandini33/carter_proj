from rest_framework import serializers
from .models import *

 


class orders_serializer(serializers.HyperlinkedModelSerializer):
  
    class Meta:
        model = orders
        fields = '__all__'

class customers_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = customers
        fields = '__all__'

class products_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = products
        fields = '__all__'

