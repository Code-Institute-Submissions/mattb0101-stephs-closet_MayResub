from django.shortcuts import render


def user_profile(request):
    """ display users profile """
    context = {}

    return render(request, 'profile/profile.html', context)
