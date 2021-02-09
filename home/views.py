from django.shortcuts import render


def index(request):
    """ View to create index page return """
    return render(request, 'home/index.html')
