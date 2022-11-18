from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('staff/',views.staff,name='staff'),
    path('order/',views.order1,name='order'),
    path('products/',views.products,name='products'),
    path('Stock/',views.stock,name='stock'),
    path('inventory',views.inventory,name='inventory-page'),
    path('inventory/<int:pk>',views.inv_history,name='inventory-history-page'),
    path('suppliers/',views.supplier,name='suppliers'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    
]
