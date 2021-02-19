from django.shortcuts import render, redirect, reverse, HttpResponse


def view_cart(request):
    """ View to return cart page"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ add item and quantity to the cart"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'size' in request.POST:
        size = request.POST['size']
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['item_with_size'].keys():
                cart[item_id]['item_with_size'][size] += quantity
            else:
                cart[item_id]['item_with_size'][size] = quantity
        else:
            cart[item_id] = {'item_with_size': {size: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart

    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Update items already in the cart """

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'size' in request.POST:
        size = request.POST['size']
    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            cart[item_id]['item_with_size'][size] = quantity
        else:
            del cart[item_id]['item_with_size'][size]
            if not cart[item_id]['item_with_size']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Update items already in the cart """

    try:
        size = None
        if 'size' in request.POST:
            size = request.POST['size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['item_with_size'][size]
            if not cart[item_id]['item_with_size']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
        