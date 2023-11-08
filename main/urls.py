from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('delivery/', views.delivery, name='delivery')
]