from django.urls import path
# this imports views/py from current directory
from . import views

urlpatterns = [
    path('', views.stock, name='stock'),
    path('update/<int:item_id>', views.update_stock, name='update_stock'),
    path('receive/<int:item_id>', views.receive_stock, name='receive_stock'),
    path('issue/<int:item_id>', views.issue_stock, name='issue_stock'),
]
