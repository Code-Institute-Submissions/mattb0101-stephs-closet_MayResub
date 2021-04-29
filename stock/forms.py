from django import forms
from .models import StockTransactions
from products.models import Product


class SearchForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name']


class UpdateStock(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['in_stock']

    def __init__(self, *args, **kwargs):
        """
        Put in customised form and remove labels
        """
        super().__init__(*args, **kwargs)
        self.fields['in_stock'].label = False
