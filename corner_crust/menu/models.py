from django.db import models


class Category(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100)


class Product(models.Model):
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    name = models.CharField(max_length=100, unique=True)
    product_slug = models.SlugField(max_length=40, unique=True, null=True)
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, related_name='products')
    price = models.DecimalField(max_digits=13, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    in_stock = models.PositiveIntegerField(default=0)
    discount = models.PositiveSmallIntegerField(default=0)

    def get_price(self):
        if self.discount:
            return round(self.price / 100 * (100 - self.discount), 2)
        return self.price


class Pizza(models.Model, Product):
    size = models.CharField(max_length=10)

    # (json or dict like {} as default then may be {cheese: 1}, then e.g. {cheese: 2, pickles: 1} etc.)
    toppings = models.JSONField()
