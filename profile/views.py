from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserAccount
from .forms import UserAccountForm


def user_profile(request):
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
