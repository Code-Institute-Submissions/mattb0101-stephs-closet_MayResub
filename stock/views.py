from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import StockTransactions
from .forms import SearchForm, UpdateStock

from django.contrib import messages


from products.models import Product


@login_required
def stock(request):
    """ View to show list of items and stock """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! thats for the store management only!')
        return redirect(reverse('home'))

    products = Product.objects.all()
    list_search = None

    if request.GET:
        if 'list_search' in request.GET:
            list_search = request.GET['list_search']
            if not list_search:
                messages.error(request, "There is nothing to search on!")
                return redirect(reverse('product_list'))

            list_searches = Q(category__cat_name__icontains=list_search) | Q(name__icontains=list_search)
            products = products.filter(list_searches)

    paginator = Paginator(products, 50)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': products,
        'paginator': paginator,
        'page_obj': page_obj,
    }
    return render(request, 'stock/stock.html', context)


def update_stock(request, item_id):
    """ Update stock of an item manually """

    product = get_object_or_404(Product, pk=item_id)
    form = UpdateStock()

    context = {
        'product': product,
        'form': form
    }

    return render(request, 'stock/update-stock.html', context)
