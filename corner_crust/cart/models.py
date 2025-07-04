from django.db import models
from users.models import User
from menu.models import Product


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='carts')
    is_ordered = models.BooleanField(default=False)


class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    quantity = models.PositiveSmallIntegerField(default=0)
