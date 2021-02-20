from django.shortcuts import render, redirect
from .models import Stock


def stock(request):
    """ View to show list of items and stock """

    stock = Stock.objects.all()

    context = {
        'stock': stock,
    }

    return render(request, 'stock/stock.html', context)


def update_stock(request, item_id):
    """ Update the stock for an individual item manually """

    stock = Stock.objects.all()

    context = {
        'stock': stock,
    }

    return redirect('stock/stock.html')
