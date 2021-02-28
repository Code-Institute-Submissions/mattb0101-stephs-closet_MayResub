from django.db import models

from products.models import Product


class Stock(models.Model):
    product = models.ForeignKey(Product, max_length=254, blank=False, null=False, on_delete=models.CASCADE)
    in_stock = models.IntegerField(blank=True, null=True, default=0)
    issue_qty = models.IntegerField(blank=True, null=True, default=0)
    receive_qty = models.IntegerField(blank=True, null=True, default=0)

    def update_on_sale(self):
        """ Update in Stock value with order qty """
        self.in_stock = self.in_stock - self.issue_qty
        self.save()

    def __int__(self):
        return self.in_stock
