from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Stock


def stock(request):
    """ View to show list of items and stock """

    stock = Stock.objects.all()

    context = {
        'stock': stock,
    }

    return render(request, 'stock/stock.html', context)


def update_stock(request, item_id):
    """ Update stock of an item manually """

    stock = get_object_or_404(Stock, pk=item_id)

    context = {
        'stock': stock,
    }

    return render(request, 'stock/update-stock.html', context)
