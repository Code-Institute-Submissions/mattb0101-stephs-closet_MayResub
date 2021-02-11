from django.shortcuts import render
from .models import Product


def all_products(request):
    """ A master page for all products, will have sorting and searching for products """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
