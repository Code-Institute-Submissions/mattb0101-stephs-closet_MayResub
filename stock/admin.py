from django.contrib import admin
from .models import Stock


class StockAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'in_stock',
    )


admin.site.register(Stock, StockAdmin)
