from _decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Product
from .cart import Cart
from .forms import CartAddProductForm, OrderCreate
from .models import OrderProduct


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True})
    return render(request, 'cart/detail.html', {'cart': cart})


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreate(request.POST)
        if form.is_valid():
            order = form.save()
            order.total_sum = cart.get_total_price()
            order.save()
            # message = 'Спасибо! Заказ оформлен'
            for item in cart:
                OrderProduct.objects.create(order=order,
                                            order_product=item['product'],
                                            price=item['price'],
                                            quantity=item['quantity'])
            cart.clear()
            return render(request, 'cart/created.html', {'order': order})
    else:
        form = OrderCreate()
        # message = 'Заполните форму'
    return render(request, 'cart/product_detail.html', {'form': form})
