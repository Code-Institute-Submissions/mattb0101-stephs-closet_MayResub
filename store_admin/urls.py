from django.urls import path
# this imports views/py from current directory
from . import views

urlpatterns = [
    path('', views.store_admin, name='store_admin'),
    path('api/chart/data/', views.AdminChartData.as_view()),
    path('add/', views.add_product, name='add_product'),
    path('list/', views.product_list, name='product_list'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
