from django.urls import path
# this imports views/py from current directory
from . import views

urlpatterns = [
    path('', views.store_admin, name='store_admin'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
]
