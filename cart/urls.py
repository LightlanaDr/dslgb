from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<slug:product_id>/', views.cart_add, name='cart_add'),
    path('remote/<slug:product_id>/',  views.cart_remove, name='cart_remove'),
    path('order_create/', views.order_create, name='order_create'),
    path('created/', views.order_create, name='created'),
]

