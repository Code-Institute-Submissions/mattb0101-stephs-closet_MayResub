from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Sub_Category


def all_products(request):
    """ A master page for all products,
    will have sorting and searching for products.
    """

    products = Product.objects.all()
    search = None
    categories = None
    sub_categories = None
    sort = None
    direction = None

    if request.GET:
        print(request.GET)
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey == 'category__cat_name'
            if sortkey == 'sub_category':
                sortkey == 'sub_category__subcat_name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__cat_name__in=categories)
            categories = Category.objects.filter(cat_name__in=categories)

        if 'sub_category' in request.GET:
            sub_categories = request.GET['sub_category'].split(',')
            products = products.filter(
                subcat__subcat_name__in=sub_categories)
            sub_categories = Sub_Category.objects.filter(
                subcat_name__in=sub_categories)

        if 'search' in request.GET:
            search = request.GET['search']
            if not search:
                messages.error(request, "There is nothing to search on!")
                return redirect(reverse('products'))

            searches = Q(name__icontains=search)
            products = products.filter(searches)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': search,
        'current_categories': categories,
        'current_sub_categories': sub_categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_info(request, item_id):
    """ Single product info page that allows user to buy """

    product = get_object_or_404(Product, pk=item_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)


