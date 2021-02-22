from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from checkout.models import Order
from .models import UserAccount
from .forms import UserAccountForm


def user_account(request):
    """ display users profile """
    account = get_object_or_404(UserAccount, user=request.user)

    if request.method == "POST":
        form = UserAccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserAccountForm(instance=account)
    orders = account.orders.all

    context = {
        'form': form,
        'orders': orders,
        'on_account': True
    }

    return render(request, 'profile/profile.html', context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past order for order {order_number}.'
    ))
    context = {
        'order': order,
        'history': True,
    }

    return render(request, 'checkout/checkout_success.html', context)
