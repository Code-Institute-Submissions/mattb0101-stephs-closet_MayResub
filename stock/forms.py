from django import forms
from .models import StockTransactions
from products.models import Product


class SearchForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name']


class UpdateStock(forms.ModelForm):
    class Meta:
        model = StockTransactions
        fields = ['amount']

    def __init__(self, *args, **kwargs):
        """
        Put in customised form and remove labels
        """
        super().__init__(*args, **kwargs)
        self.fields['amount'].label = False
