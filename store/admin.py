from itertools import product
from django.contrib import admin
from .models import Category, Product

class AdminCategory(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class AdminProduct(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)