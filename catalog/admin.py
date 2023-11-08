from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price']
    list_filter = ['category', 'price']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_cat', 'status']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

