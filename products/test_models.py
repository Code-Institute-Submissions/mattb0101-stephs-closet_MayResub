from django.test import TestCase
from .models import Product


class TestModels(TestCase):

    def test_stock_default_level(self):
        product = Product.objects.create(name="Test Item")
        self.assertTrue(product.in_stock == 0)
