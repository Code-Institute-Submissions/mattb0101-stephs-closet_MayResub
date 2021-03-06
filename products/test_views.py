from django.test import TestCase
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Product


class TestViews(TestCase):

    def test_get_all_products(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_info_page(self):
        with self.assertRaises(Http404):
            get_object_or_404(Product, name="Run")

        product = Product.objects.create(name="Test Item")
        self.assertEqual(
            get_object_or_404(Product, pk=product.id),
            product
        )
        # response = self.client.get(f'/products/{product.id}/')
        # self.assertEqual(response.status_code, 404)
        # self.assertTemplateUsed(response, 'products/product_info.html')
