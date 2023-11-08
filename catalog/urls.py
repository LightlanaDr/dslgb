from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_products, name='category_products'),
    path('<slug:category_slug>/', views.cat_slug_products, name='cat_slug_products'),
    # path('test/<int:id>/', views.product_detail, name='product_detail'),
]
