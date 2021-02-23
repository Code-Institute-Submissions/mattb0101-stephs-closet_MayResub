from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ProductForm
from django.contrib import messages

from products.models import Product


def store_admin(request):
    """ View to create index page return """
    return render(request, 'store_admin/store_admin.html')


def add_product(request):
    """ Add a new product """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added new Product')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add new product')
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'store_admin/add_product.html', context)


def edit_product(request, product_id):
    """ Edit a product """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Product!')
            return redirect(reverse('store_admin'))
        else:
            messages.error(request, 'Failed')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'store_admin/edit_product.html', context)
