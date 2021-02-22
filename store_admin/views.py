from django.shortcuts import render, redirect, reverse
from .forms import ProductForm
from django.contrib import messages


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
