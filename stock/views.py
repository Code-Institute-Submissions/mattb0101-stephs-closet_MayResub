from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Stock
from .forms import SearchForm, AddStock, RemoveStock

from django.contrib import messages


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

    item = get_object_or_404(Stock, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'stock/update-stock.html', context)


def issue_stock(request, item_id):
    """ Issue Stock of Item """

    item = get_object_or_404(Stock, pk=item_id)
    form = RemoveStock(request.POST or None, instance=item)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.in_stock -= instance.issue_qty
        messages.success(request, 'Issued Stock')
        instance.save()

        return redirect(reverse('update_stock', args=[item.product.id]))

    context = {
        'item': item,
        'form': form,
    }
    return render(request, 'stock/issue-stock.html', context)


def receive_stock(request, item_id):
    """ Receive Stock of Item """

    item = get_object_or_404(Stock, pk=item_id)
    form = AddStock(request.POST or None, instance=item)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.in_stock += instance.receive_qty
        messages.success(request, 'Received Stock')
        instance.save()

        return redirect(reverse('update_stock', args=[item.product.id]))

    context = {
        'item': item,
        'form': form,
    }
    return render(request, 'stock/receive-stock.html', context)
