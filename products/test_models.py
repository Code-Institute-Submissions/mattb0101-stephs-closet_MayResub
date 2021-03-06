from django.test import TestCase
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Product


class TestModels(TestCase):

    def test_stock_default_level(self):
        product = Product.objects.create(name="Test Item")
        self.assertTrue(product.in_stock == 0)
