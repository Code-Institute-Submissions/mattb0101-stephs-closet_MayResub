from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_cart(request):
    """ View to return cart page"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ add item and quantity to the cart"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if quantity > product.in_stock:
        messages.error(request, f'Not enough stock of {product.name} to add this item to your cart \
                                  please decrease the quantity.')
        return redirect(redirect_url)
    else:
        if 'size' in request.POST:
            size = request.POST['size']
        cart = request.session.get('cart', {})

        if size:
            if item_id in list(cart.keys()):
                if size in cart[item_id]['item_with_size'].keys():
                    cart[item_id]['item_with_size'][size] += quantity
                    messages.success(request, f'Updated {size} {product.name} to your cart')
                else:
                    cart[item_id]['item_with_size'][size] = quantity
                    messages.success(request, f'Added {size} {product.name} to your cart')
            else:
                cart[item_id] = {'item_with_size': {size: quantity}}
                messages.success(request, f'Added size {size} {product.name} to your cart')
        else:
            if item_id in list(cart.keys()):
                cart[item_id] += quantity
                messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
            else:
                cart[item_id] = quantity
                messages.success(request, f'Added {product.name} to your cart')

        request.session['cart'] = cart
        return redirect(redirect_url)


def update_cart(request, item_id):
    """ Update items already in the cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None

    if quantity > product.in_stock:
        messages.error(request, f'Not enough stock of {product.name} to increase the quantity in \
                                  your cart.')
        return redirect(reverse('view_cart'))
    else:
        if 'size' in request.POST:
            size = request.POST['size']
        cart = request.session.get('cart', {})

        if size:
            if quantity > 0:
                cart[item_id]['item_with_size'][size] = quantity
                messages.success(request, f'Updated {product.name} quantity in your bag')
            else:
                del cart[item_id]['item_with_size'][size]
                if not cart[item_id]['item_with_size']:
                    cart.pop(item_id)
                    messages.success(request, f'Removed {product.name} quantity in your bag')
        else:
            if quantity > 0:
                cart[item_id] = quantity
                messages.success(request, f'Updated {product.name} quantity in your bag')
            else:
                cart.pop(item_id)
                messages.success(request, f'Removed {product.name} to your bag')

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Update items already in the cart """

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'size' in request.POST:
            size = request.POST['size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['item_with_size'][size]
            if not cart[item_id]['item_with_size']:
                cart.pop(item_id)
                messages.success(request, f'Removed {product.name} quantity in your bag')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} quantity in your bag')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.success(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
