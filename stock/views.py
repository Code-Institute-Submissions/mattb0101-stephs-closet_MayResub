from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Stock
from .forms import SearchForm

from products.models import Product


def stock(request):
    """ View to show list of items and stock """

    stock = Stock.objects.all()
    form = SearchForm(request.POST or None)

    context = {
        'stock': stock,
        'form': form,
    }
    if request.method == "POST":
        stock = Stock.objects.filter(
            product__icontains=form['product'].value())

        context = {
            'form': form,
            'stock': stock,
        }
    return render(request, 'stock/stock.html', context)


def update_stock(request, item_id):
    """ Update stock of an item manually """

    item = get_object_or_404(Product, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'stock/update-stock.html', context)
