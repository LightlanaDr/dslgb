from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.views import View
from .models import Product, Category
from django.contrib.auth.hashers import check_password
from cart.forms import CartAddProductForm


def category_products(request):
    """ Представление для списка категорий и продуктов"""
    # category_slug = None
    status = 'Опубликовано'
    categories = Category.objects.filter(status=status).all()
    category = None
    products = Product.objects.all()
    form = CartAddProductForm()
    return render(request, 'catalog/product_detail.html', {'category': category, 'categories': categories,
                                                           'products': products,
                                                           "form": form})


def cat_slug_products(request, category_slug=None):
    """ Представление для списка категорий и продуктов по категориям"""
    status = 'Опубликовано'
    categories = Category.objects.filter(status=status).all()
    category = None
    products = None
    form = CartAddProductForm()
    if category_slug:
        category = Category.objects.get(id=category_slug)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    return render(request, 'catalog/product_detail.html', {'category': category, 'categories': categories,
                                                     'products': products,
                                                     "form": form})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    form = CartAddProductForm()
    return render(request, 'catalog/test.html', {"product": product,
                                                           "form": form})



