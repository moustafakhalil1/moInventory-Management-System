from django.contrib import admin
from dashboard.models import order, product,stock,suppliers,Stockproduct
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header='invetory shop'
class projectadmin(admin.ModelAdmin):
    list_display=('id','name','category')
    list_filter=[
        'category'
    ]
class projectadmin2(admin.ModelAdmin):
    list_display=('id','product','staff',"category",'date')
    list_filter=[
        'date'
    ]
# Register your models here.
admin.site.register(product,projectadmin)
admin.site.register(order)
admin.site.register(suppliers)
admin.site.register(stock)
admin.site.register(Stockproduct)



