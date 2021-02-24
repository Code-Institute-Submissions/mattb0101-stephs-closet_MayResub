from django.urls import path
# this imports views/py from current directory
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<item_id>/', views.product_info, name='product_info')
]
