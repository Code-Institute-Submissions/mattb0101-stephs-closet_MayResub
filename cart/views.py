from django.shortcuts import render, redirect


def view_cart(request):
    """ View to return cart page"""

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ add item and quantity to the cart"""

    if request.method == "POST":
        print(request.POST)

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
