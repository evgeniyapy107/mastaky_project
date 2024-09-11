from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'address', 'phone', 'comment',
            'payment_method', 'delivery_method', 'delivery_date', 'delivery_time'
        ]
        widgets = {
            'delivery_date': forms.SelectDateWidget(),
            'delivery_time': forms.Select(choices=Order.DELIVERY_TIME_CHOICES),
            'payment_method': forms.RadioSelect(choices=Order.PAYMENT_METHOD_CHOICES),
            'delivery_method': forms.RadioSelect(choices=Order.DELIVERY_METHOD_CHOICES),
        }

