import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','schema2_design.settings')
import django
django.setup()
import random
from base1.models import *
from faker import Faker
import numpy as np 
fake = Faker()

class random_data:
    def __init__ (self):
        pass
    
    def Name(self):
        return fake.name()

    def iden(self):
        id = [i for i in range(100,1000)]
        return np.random.choice(id)

    def age(self):
        age = [i for i in range(20,50)]
        return np.random.choice(age)

    def quantity(self):
        quan = [i for i in range(1,100)]
        return np.random.choice(quan)

    def gender(self):
        gender = ("M", "F", "O")
        return np.random.choice(gender)

    def phone_no(self):
        return fake.phone_number()

    def address(self):
        return fake.address()

    def cost(self):
        return random.randint(100,10000)

    def unit_cost(self):
        return random.randint(10,100)
    
    def discount(self):
        return random.randint(2,30)
    
    def fees(self):
        return random.randint(10,100)

    def mail(self):
        return fake.email()

    def payment(self):
        pay = ['COD', 'CREDIT', 'DEBIT', 'NETBANKING', 'PAYPAL']
        return np.random.choice(pay)

    def cate_name(self):
        names=['baked','hand_made']
        return np.random.choice(names)

    def bank(self):
        names=['SBI','PNB','BOB','HDFC','ICICI']
        return np.random.choice(names)

    def pname(self):
        names=['white_choc','dark_choc','coffee_choc','sea-salt']
        return np.random.choice(names)

rd = random_data()

def cate_id(str):
    if str=='baked':
        return 1
    else:
        return 2


def product_id(str):
    if str=='white_choc':
        return 10
    elif str=='dark_choc':
        return 20
    elif str=='coffee_choc':
        return 30
    else:
        return 40

def prod_Details():
        return {str(product_id(rd.pname())):rd.discount() ,str(product_id(rd.pname())):rd.discount()}

def populate_customers():
    
        id_k = rd.iden()
        o1 = customers.objects.get_or_create(c_id = id_k ,
                                             name = rd.Name(),age = rd.age(),gender = rd.gender(),
                                             phone_no = rd.phone_no(),
                                             address = rd.address(), address_id= rd.iden(),
                                             mailid = rd.mail())
        
        return o1

def populate_orders(n=5):
    for i in range(n):
        p= rd.payment()
        prod = rd.pname()
        o2 = orders.objects.get_or_create(order_id = rd.iden(),date_created = fake.date() , customer_fees = rd.fees() ,discounts = rd.discount(),
                                                subtotal = rd.cost() , transaction_amount = rd.cost() , timestamp = fake.iso8601(),
                                                bank = rd.bank() , transaction_id = rd.iden() ,paymethod  = p,
                                                address_id = populate_customers()[0] , product_details = prod_Details())
       
    return o2

def populate_products():
    for i in range(4):
         c = rd.cate_name()
         p = rd.pname()
         o3 = products.objects.get_or_create(  product_id = product_id(p) , product_name = p ,unit_price = rd.unit_cost() ,
                                                category_id = cate_id(c), supplier_id = rd.iden() ,wholesale_price = rd.unit_cost()-5 ,
                                                category = c ,supplier_phone = rd.phone_no() , supplier_name = rd.Name() ,
                                                product_quantity = rd.discount() , supplier_address = rd.address())   
         
    return o3


