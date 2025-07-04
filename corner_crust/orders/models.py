from django.db import models
from users.models import User
from cart.models import Cart, CartItem


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='orders')
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE, related_name='order')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    requires_delivery = models.BooleanField(default=False)
    delivery_address = models.TextField(max_length=150, null=True, blank=True)
    payment_on_get = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=20, default='В обработке')


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name='items')
    cart_item = models.ForeignKey(to=CartItem, on_delete=models.CASCADE, related_name='order_item')
