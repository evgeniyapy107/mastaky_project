from django.conf import settings
from decimal import Decimal
from painting import models


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, painting):
        painting_id = str(painting.id)
        if painting_id not in self.cart:
            self.cart[painting_id] = {'quantity': 1, 'price': str(painting.price)}
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, painting):
        painting_id = str(painting.id)
        if painting_id in self.cart:
            del self.cart[painting_id]
            self.save()

    def __iter__(self):
        painting_ids = self.cart.keys()
        paintings = models.Painting.objects.filter(id__in=painting_ids)
        for painting in paintings:
            self.cart[str(painting.id)]['painting'] = painting
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
