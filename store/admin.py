from django.contrib import admin
from .models import *
# Register your models here.
# anthonymensah1030@gmail.com, admin, projectpass1030 or
# admin@gmail.com,

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'is_active']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'in_stock']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'cost', 'complete']

@admin.register(Orderitem)
class OrderitemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'subtotal']
