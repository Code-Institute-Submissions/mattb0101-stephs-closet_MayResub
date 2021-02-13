from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """ A master page for all products,
    will have sorting and searching for products.
    """

    products = Product.objects.all()
    search = None

    if request.GET:
        if 'search' in request.GET:
            search = request.GET['search']
            if not search:
                messages.error(request, "There is nothing to search on!")
                return redirect(reverse('products'))

            searches = Q(name__icontains=search)
            products = products.filter(searches)

    context = {
        'products': products,
        'search_term': search,
    }

    return render(request, 'products/products.html', context)


def product_info(request, item_id):
    """ Single product info page that allows user to buy """

    product = get_object_or_404(Product, pk=item_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)


