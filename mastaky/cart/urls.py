from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:painting_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:painting_id>/', views.cart_remove, name='cart_remove'),
    path('order/', views.order_create, name='order'),
    path('order_success/', views.order_success, name='order_success')
]
