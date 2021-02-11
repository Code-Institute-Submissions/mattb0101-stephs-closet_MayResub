from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ A master page for all products, will have sorting and searching for products """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_info(request, item_id):
    """ Single product info page that allows user to buy """

    product = get_object_or_404(Product, pk=item_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)


