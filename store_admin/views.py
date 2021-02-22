from django.shortcuts import render

from .forms import ProductForm


def store_admin(request):
    """ View to create index page return """
    return render(request, 'store_admin/store_admin.html')


def add_product(request):
    """ Add a new product """
    form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'store_admin/add_product.html', context)
