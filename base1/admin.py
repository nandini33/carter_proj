from django.contrib import admin

from .models import *

admin.site.register(customers)
admin.site.register(orders)
admin.site.register(products)
