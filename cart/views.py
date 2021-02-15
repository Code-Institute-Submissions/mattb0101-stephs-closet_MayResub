from django.shortcuts import render


def view_cart(request):
    """ View to return cart page"""

    return render(request, 'cart/cart.html')
