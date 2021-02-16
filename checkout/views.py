from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in the cart to checkout")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IGOjBGOUjQjPXgdd2fKB37QuCgvdtHCf2i2FHvHLgKVwNj9yWqyrwmV98ZRtodfTMcNlaATNQWuSx7UsdpmchVS00EUVyqTkq',
        'client_secret': 'test_client_secret'
    }

    return render(request, template, context)
    