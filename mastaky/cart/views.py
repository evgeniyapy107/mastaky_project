from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from painting import models
from .cart import Cart
from .forms import OrderForm
from .models import Order, OrderItem


@require_POST
def cart_add(request, painting_id):
    cart = Cart(request)
    painting = get_object_or_404(models.Painting, id=painting_id)
    cart.add(painting=painting)
    return redirect('cart:cart_detail')


def cart_remove(request, painting_id):
    cart = Cart(request)
    painting = get_object_or_404(models.Painting, id=painting_id)
    cart.remove(painting)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'detail.html', {'cart': cart})


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    painting=item['painting'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()  # Очистка корзины после создания заказа
            return redirect('cart:order_success')
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form, 'cart': cart})


def order_success(request):
    return render(request, 'order_success.html')

