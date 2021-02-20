from django.urls import path
# this imports views/py from current directory
from . import views

urlpatterns = [
    path('', views.stock, name='stock')
]
