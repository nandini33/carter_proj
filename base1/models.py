from django.db import models
import datetime
# Create your models here.
class customers (models.Model):
    c_id = models.BigIntegerField( null = False ,default = 1)
    name  = models.CharField(max_length = 20)
    age = models.BigIntegerField()
    gender = models.CharField(max_length = 10)
    mailid = models.CharField(max_length = 80)
    phone_no = models.CharField(max_length = 80)
    address = models.CharField(max_length = 80)
    address_id = models.BigIntegerField(unique = True, null = False , default = 1)
 
    def __str__(self):
        return str(self.address_id)

class orders (models.Model):
    order_id = models.BigIntegerField(unique = True, null = False , default = 1)
    date_created = models.DateField()
    customer_fees = models.BigIntegerField()
    discounts = models.BigIntegerField()
    subtotal = models.BigIntegerField()
    transaction_amount = models.BigIntegerField(default=200)
    timestamp = models.DateTimeField(default = '')
    bank = models.CharField(max_length=20 ,default='SBI')
    transaction_id = models.BigIntegerField()
    paymethod  = models.CharField(max_length = 20 ,default='COD')
    address_id = models.ForeignKey('customers', on_delete=models.CASCADE)
    product_details = models.JSONField(default = dict (product_id = [],product_quantity = []))

    def __str__(self):
        return str(self.address_id)

class products (models.Model):
    product_id = models.BigIntegerField(null = False , default = 1 )
    product_name = models.CharField(max_length = 30)
    unit_price = models.BigIntegerField()
    category_id = models.BigIntegerField()
    supplier_id = models.BigIntegerField()  
    wholesale_price = models.BigIntegerField()
    category = models.CharField(max_length = 30, default='baked')
    supplier_phone = models.CharField(max_length = 80, default='xyz')
    supplier_name = models.CharField(max_length = 30 ,default='xyz')
    product_quantity = models.BigIntegerField(default=10)
    supplier_address = models.CharField(max_length = 30, default='india')   
    def __str__(self):
        return str(self.product_id)  

