from django.shortcuts import render


def stock(request):
    """ View to create index page return """
    return render(request, 'stock/stock.html')
