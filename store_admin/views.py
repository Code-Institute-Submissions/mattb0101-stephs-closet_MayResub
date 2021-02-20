from django.shortcuts import render


def store_admin(request):
    """ View to create index page return """
    return render(request, 'store_admin/store_admin.html')
