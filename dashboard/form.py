from dataclasses import field, fields
from pyexpat import model
from xml.dom.minidom import Attr
from .models import order, product,suppliers,stock,Stockproduct
from django import forms
class product_forms(forms.ModelForm):
    class Meta:
        model=product
        fields=[
            'code',
            'name',
            'category',
            

           
        ]
        widgets = {
              'code':forms.NumberInput(attrs={'class':'form-control'}),
              'name':forms.TextInput(attrs={'class':'form-control'}),
              'category':forms.Select(attrs={'class':'form-control'}),    

        }
    def clean_code(self):
        id = self.instance.id if self.instance.id else 0
        code = self.cleaned_data['code']
        try:
            if int(id) > 0:
                product = product.objects.exclude(id=id).get(code = code)
            else:
                product = product.objects.get(code = code)
        except:
            return code
        raise forms.ValidationError(f"{code} Category Already Exists.")

class order_form(forms.ModelForm):
    class Meta:
        model=Stockproduct
        fields=[
            'product',
            'quantity',
            'type',
        ] 

        widgets = {
              'product':forms.Select(attrs={'class':'form-control'}),
              'quantity':forms.NumberInput(attrs={'class':'form-control'}),
              'type':forms.Select(attrs={'class':'form-control'}),
                           
        }
class suppliers_form(forms.ModelForm):
    class Meta:
        model=suppliers
        fields=[
            'supname',
            'suppCity',
            'suppaddress',
            'supphone',   
        ] 

        widgets = {
              'supname':forms.TextInput(attrs={'class':'form-control'}),
              'suppCity':forms.TextInput(attrs={'class':'form-control'}),
              'suppaddress':forms.TextInput(attrs={'class':'form-control'}),
              'supphone':forms.NumberInput(attrs={'class':'form-control'}),
        }
class stock_form(forms.ModelForm):
    class Meta:
        model=stock
        fields=[
            'stoname',
            'stoCity',
            'stoaddress',
            'stostatus',
            'stophone',   
        ] 

        widgets = {
              'stoname':forms.TextInput(attrs={'class':'form-control'}),
              'stoCity':forms.TextInput(attrs={'class':'form-control'}),
              'stoaddress':forms.TextInput(attrs={'class':'form-control'}),
              'stostatus':forms.Select(attrs={'class':'form-control'}),
              'stophone':forms.NumberInput(attrs={'class':'form-control'}),
             
        }
    def clean_name(self):
        id = self.instance.id if self.instance.id else 0
        name = self.cleaned_data['stoname']
        # print(int(id) > 0)
        # raise forms.ValidationError(f"{name} Category Already Exists.")
        try:
            if int(id) > 0:
                category = stock.objects.exclude(id=id).get(stoname = name)
            else:
                category = stock.objects.get(stoname = name)
        except:
            return name
            # raise forms.ValidationError(f"{name} Category Already Exists.")
        raise forms.ValidationError(f"{name} Category Already Exists.")
class SaveStock(forms.ModelForm):
    
    class Meta:
        model = Stockproduct
        fields=[
            'product',
            'quantity',
            'type',   
        ]
        widgets = {
              'product':forms.Select(attrs={'class':'form-control'}),
              'quantity':forms.NumberInput(attrs={'class':'form-control'}),
              'type':forms.Select(attrs={'class':'form-control'}),         
             
        } 

    def clean_product(self):
        pid = self.cleaned_data['product']
        try:
            Product = product.objects.get(id=pid)
            print(Product)
            return Product
        except:
            raise forms.ValidationError("Product is not valid")
