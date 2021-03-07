from django.urls import path
# this imports views/py from current directory
from . import views

urlpatterns = [
    path('', views.user_account, name='user_account'),
    path(
        'order_history/<order_number>',
        views.order_history, name='order_history'
    ),
]
