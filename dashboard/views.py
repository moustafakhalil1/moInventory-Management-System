from django.shortcuts import render

# Create your views here.
from math import prod
from django.db.models.query_utils import RegisterLookupMixin
from django.shortcuts import render,redirect,get_object_or_404
from .models import product,order,Stockproduct,suppliers
from django.contrib.auth.decorators import login_required
from .form import order_form, product_forms,suppliers_form,stock_form,SaveStock
from django.contrib.auth.models import User
#some library
from email import message

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

import json
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.conf import settings
import base64

# Create your views here.


@login_required(login_url='user-login')
def home(request):
    from .models import order

    if request.method=='POST':
        add_order=order_form(request.POST)
        if add_order.is_valid():
            add_order.save()
    context={
        'order':order.objects.all(),
        'stocks':Stockproduct.objects.filter(type='1').count(),
        'stockedout':Stockproduct.objects.filter(type='2').count(),
        'form':order_form(),
        'products':product.objects.all(),
        'allsuppliers':suppliers.objects.count(),
        
    }
    return render(request,'dashboard/index.html',context)

@login_required(login_url='user-login')    
def staff(request):
    context={
       'user':User.objects.all(),
    }
    return render(request,'dashboard/staff.html',context)    
@login_required(login_url='user-login')
def order1(request):
    if request.method=='POST':
        add_order=order_form(request.POST)
        if add_order.is_valid():
            add_order.save()            
            return redirect('order')     
    context={
        'form':order_form(),
        'orderform':Stockproduct.objects.all(),
    }
    return render(request,'dashboard/order.html',context) 
@login_required(login_url='user-login')
def products(request):
    if request.method=='POST':
        add_product=product_forms(request.POST)
        if add_product.is_valid():
            add_product.save()
            return redirect('products')
    context={
        'product':product.objects.all(),
        'form':product_forms(),
    }
    return render(request,'dashboard/products.html',context) 
#Inventory
@login_required
def inventory(request):
  
    products = product.objects.all()
    context={
        'products':products,
      }
    return render(request, 'dashboard/inventory.html',context)
@login_required
def inv_history(request, pk= None):

    if pk is None:
        messages.error(request, "Product ID is not recognized")
        return redirect('inventory-page')
    else:
        Product = product.objects.get(id = pk)
        stocks = Stockproduct.objects.filter(product = Product).all()
        context={
        'product':Product,
        'stocks':stocks,
        }

        return render(request, 'dashboard/inventory_history.html', context )
@login_required(login_url='user-login')
def supplier(request):
     if request.method=='POST':
        add_product=suppliers_form(request.POST)
        if add_product.is_valid():
            add_product.save()
     context={
        'form':suppliers_form(),
      }

     return render(request,'dashboard/suppliers.html',context)

@login_required
def manage_stock(request,pid = None ,pk = None):
    if pid is None:
        messages.error(request, "Product ID is not recognized")
        return redirect('inventory-page')
    context['pid'] = pid
    if pk is None:
        context['page_title'] = "Add New Stock"
        context['stock'] = {}
    else:
        context['page_title'] = "Manage New Stock"
        stockproduct = Stock.objects.get(id = pk)
        context['stock'] = stock
    
    return render(request, 'manage_stock.html', context )

@login_required(login_url='user-login')
def stock(request):
    if request.method=='POST':
        add_stock=stock_form(request.POST)
        if add_stock.is_valid():
            add_stock.save()
    context={
        'form':stock_form(),
      }

    return render(request,'dashboard/stocks.html',context)


@login_required(login_url='user-login')        
def update(request,id):
      from .models import product
      product_id=product.objects.get(id=id)
      if request.method=='POST':
         product_save=product_forms(request.POST,instance=product_id)
         if product_save.is_valid():
              product_save.save()
              return redirect('products')
      else:
         product_save=product_forms(instance=product_id)
      context={
        'form':product_save,
      }   
      
      return render(request ,'dashboard/update.html',context)
@login_required(login_url='user-login')
def delete(request,id):
      from .models import product
      product_delete=get_object_or_404(product,id=id)
      if request.method=='POST':
        product_delete.delete()
        return redirect('products')
      return render(request ,'dashboard/delete.html') 


