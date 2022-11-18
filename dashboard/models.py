from django.db import models

# Create your models here.
from pyexpat import model
from tabnanny import verbose
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
category_choices=(
    ('stationary','stationary'),
    ('electronincs','electronics'),
    ('food','food')
)

status=(
    ('available','available'),
    ('full','full')
)
class suppliers(models.Model):
    supname=models.CharField(max_length=50,null=True,blank=True,verbose_name='Supplier name')
    suppCity=models.CharField(max_length=200,null=True,blank=True,verbose_name='Supplier City')
    suppaddress=models.CharField(max_length=200,null=True,blank=True,verbose_name='Supplier Address')
    supphone=models.IntegerField(null=True,blank=True,verbose_name='Supplier Phone Number')
    def __str__(self) -> str:
        return self.supname

class stock(models.Model):
    code=models.CharField(max_length=100,blank=True, null=True)
    stoname=models.CharField(max_length=50,null=True,blank=True,verbose_name='Stock name')
    stoCity=models.CharField(max_length=200,null=True,blank=True,verbose_name='Stock City')
    stoaddress=models.CharField(max_length=50,null=True,blank=True,verbose_name='Stock Address')
    stostatus=models.CharField(choices=status,max_length=20,null=True,blank=True,verbose_name='Stock Status')
    stophone=models.IntegerField(null=True,blank=True,verbose_name='Stock Phone Number')
    

    def __str__(self) -> str:
        return self.stoname
class product(models.Model):
    code=models.CharField(max_length=100,blank=True, null=True)
    name=models.CharField(max_length=50,null=True,verbose_name='Product name')
    category=models.CharField(choices=category_choices,max_length=20,verbose_name='product Category')
    price=models.DecimalField(max_digits=6,decimal_places=3,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.name
    def count_inventory(self):
        stocks = Stockproduct.objects.filter(product = self) 
        stockIn = 0
        stockOut = 0
        for stock in stocks:
            if stock.type == '1':
                stockIn = int(stockIn) + int(stock.quantity)
            else:
                stockOut = int(stockOut) + int(stock.quantity)
        available  = stockIn - stockOut
        return available   
    def allproducts(self):
        stocks = Stockproduct.objects.all() 
        stockIn = 0
        stockOut = 0
        for stock in stocks:
            if stock.type == '1':
                stockIn = int(stockIn) + int(stock.quantity)
            else:
                stockOut = int(stockOut) + int(stock.quantity)
        available  = stockIn - stockOut
        return available 

class Stockproduct(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(null=True)
    type = models.CharField(max_length=2,choices=(('1','Stock-in'),('2','Stock-Out')), default = 1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product.code + ' - ' + self.product.name

class order(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    staff=models.ForeignKey(User,models.CASCADE,null=True)
    quantity=models.IntegerField(null=True)
    type = models.CharField(max_length=2,choices=(('1','Stock-in'),('2','Stock-Out')), default = 1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    category=models.CharField(choices=category_choices,max_length=20,null=True)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} ordered by{self.staff}'


