from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from painting import models
from .cart import Cart


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





# Create your views here.
