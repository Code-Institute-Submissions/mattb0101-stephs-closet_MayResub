from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Product


class TestViews(TestCase):

    def test_get_all_products(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_info_page(self):
        product = get_object_or_404(Product, pk=1)
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_info.html')
