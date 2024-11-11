from django.db import models
from django.contrib.auth.models import User
from painting.models import Painting


class Order(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Наличными при получении'),
        ('erip', 'Через систему ЕРИП'),
    ]

    DELIVERY_METHOD_CHOICES = [
        ('pickup', 'Самовывоз'),
        ('post', 'Почта'),
        ('courier', 'Курьер'),
    ]

    DELIVERY_TIME_CHOICES = [
        ('morning', 'Утро'),
        ('afternoon', 'День'),
        ('evening', 'Вечер'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    comment = models.TextField(blank=True, null=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES)
    delivery_method = models.CharField(max_length=10, choices=DELIVERY_METHOD_CHOICES)
    delivery_date = models.DateField()
    delivery_time = models.CharField(max_length=10, choices=DELIVERY_TIME_CHOICES)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.painting.title} for order {self.order.id}"
