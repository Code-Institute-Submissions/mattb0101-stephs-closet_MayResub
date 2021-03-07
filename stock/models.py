from django.db import models

from products.models import Product


class StockTransactions(models.Model):
    product = models.ForeignKey(Product, max_length=254, blank=False, null=False,
    on_delete=models.CASCADE, related_name='stockproduct')
    amount = models.IntegerField(default=0)

