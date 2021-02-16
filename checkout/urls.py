from django.urls import path
# this imports views/py from current directory
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path(
        'checkout_success/<order_number>', views.checkout_success,
        name='checkout_success')
]
