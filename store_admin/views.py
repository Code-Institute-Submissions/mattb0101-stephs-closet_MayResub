from django.core.paginator import Paginator
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db import connection
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count
from django.db.models.functions import Lower

from products.models import Product, Category, Sub_Category
from checkout.models import Order, OrderLineItem

from rest_framework.views import APIView
from rest_framework.response import Response

import os


@login_required
def store_admin(request):
    """ View to create index page return """
    products = Product.objects.all()

    if not request.user.is_superuser:
        messages.error(request, 'Sorry! thats for the store management only!')
        return redirect(reverse('home'))

    context = {
        'products': products
    }

    return render(request, 'store_admin/store_admin.html', context)


class AdminChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # Query to return orders per day
        labelsNumber = []
        dataNumber = []
        labelsValue = []
        dataValue = []

        cursor = connection.cursor()

        if 'DEVELOPMENT' in os.environ:
            cursor.execute("SELECT count(order_number) AS order_count, strftime('%d-%m-%Y',date) AS date FROM checkout_order GROUP BY strftime('%d-%m-%Y',date) ORDER BY julianday('now') - julianday(date) desc")
            columns = [col[0] for col in cursor.description]
            resultsNumbers = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
            for number in resultsNumbers:
                labelsNumber.append(number['date'])
                dataNumber.append(number['order_count'])

            cursor.execute("SELECT ROUND(avg(grand_total),2) AS average_value, strftime('%d-%m-%Y',date) AS date FROM checkout_order GROUP BY strftime('%d-%m-%Y',date) ORDER BY julianday('now') - julianday(date) desc")
            columns = [col[0] for col in cursor.description]
            resultsValues = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
            for value in resultsValues:
                labelsValue.append(value['date'])
                dataValue.append(value['average_value'])

            data = {
                "ordersLabels": labelsNumber,
                "orders": dataNumber,
                "valueLabels": labelsValue,
                "avgValue": dataValue
            }
            return Response(data)
        else:
            cursor.execute('''SELECT count(order_number) AS order_count, DATE_FORMAT(date,'%d/%m/%y') AS date FROM checkout_order GROUP BY DATE_FORMAT(date,'%d/%m/%y')''')
            columns = [col[0] for col in cursor.description]
            resultsNumbers = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
            for number in resultsNumbers:
                labelsNumber.append(number['date'])
                dataNumber.append(number['order_count'])

            cursor.execute('''SELECT ROUND(avg(grand_total),2) AS average_value, DATE_FORMAT(date,'%d/%m/%y') AS date FROM checkout_order GROUP BY DATE_FORMAT(date,'%d/%m/%y')''')
            columns = [col[0] for col in cursor.description]
            resultsValues = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
            for value in resultsValues:
                labelsValue.append(value['date'])
                dataValue.append(value['average_value'])

            data = {
                "ordersLabels": labelsNumber,
                "orders": dataNumber,
                "valueLabels": labelsValue,
                "avgValue": dataValue
            }
            return Response(data)


@login_required
def product_list(request):
    """ View to create index page return """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! thats for the store management only!')
        return redirect(reverse('home'))

    products = Product.objects.all()
    list_search = None
    categories = None
    sub_categories = None
    sort = None
    direction = None

    if request.GET:
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

        if 'list_search' in request.GET:
            list_search = request.GET['list_search']
            if not list_search:
                messages.error(request, "There is nothing to search on!")
                return redirect(reverse('product_list'))

            list_searches = Q(category__cat_name__icontains=list_search)
            products = products.filter(list_searches)

    current_sorting = f'{sort}_{direction}'

    paginator = Paginator(products, 50)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': products,
        'search_term': list_search,
        'current_categories': categories,
        'current_sub_categories': sub_categories,
        'current_sorting': current_sorting,
        'paginator': paginator,
        'page_obj': page_obj,
    }

    return render(request, 'store_admin/product_list.html', context)


@login_required
def add_product(request):
    """ Add a new product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! thats for the store management only!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Added new Product')
            return redirect(reverse('product_info', args=[product.id]))
        else:
            messages.error(request, 'Failed to add new product')
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'store_admin/add_product.html', context)


@login_required
def edit_product(request, product_id):
    """ Edit a product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! thats for the store management only!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Product!')
            return redirect(reverse('edit_product', args=[product_id]))
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


@login_required
def delete_product(request, product_id):
    """ delete a product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! thats for the store management only!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('product_list'))
