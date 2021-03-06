# Generated by Django 3.1.6 on 2021-02-17 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.BigIntegerField(default=1)),
                ('name', models.CharField(max_length=20)),
                ('age', models.BigIntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('mailid', models.CharField(max_length=80)),
                ('phone_no', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=80)),
                ('address_id', models.BigIntegerField(default=1, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.BigIntegerField(default=1)),
                ('product_name', models.CharField(max_length=30)),
                ('unit_price', models.BigIntegerField()),
                ('category_id', models.BigIntegerField()),
                ('supplier_id', models.BigIntegerField()),
                ('wholesale_price', models.BigIntegerField()),
                ('category', models.CharField(default='baked', max_length=30)),
                ('supplier_phone', models.CharField(default='xyz', max_length=80)),
                ('supplier_name', models.CharField(default='xyz', max_length=30)),
                ('product_quantity', models.BigIntegerField(default=10)),
                ('supplier_address', models.CharField(default='india', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.BigIntegerField(default=1, unique=True)),
                ('date_created', models.DateField()),
                ('customer_fees', models.BigIntegerField()),
                ('discounts', models.BigIntegerField()),
                ('subtotal', models.BigIntegerField()),
                ('transaction_amount', models.BigIntegerField(default=200)),
                ('timestamp', models.DateTimeField(default='')),
                ('bank', models.CharField(default='SBI', max_length=20)),
                ('transaction_id', models.BigIntegerField()),
                ('paymethod', models.CharField(default='COD', max_length=20)),
                ('product_details', models.JSONField(default={'product_id': [], 'product_quantity': []})),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base1.customers')),
            ],
        ),
    ]
