from django.contrib import admin
from products.models import Products
# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','updated_at','created_at']
admin.site.register(Products, ProductsAdmin)