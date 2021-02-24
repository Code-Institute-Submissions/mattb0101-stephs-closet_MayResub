from django.shortcuts import render


def index(request):
    """ View to create index page return """
    return render(request, 'home/index.html')


def email(request):
    """ view to take to email page to email questions to the store """
    return render(request, 'home/email.html')
