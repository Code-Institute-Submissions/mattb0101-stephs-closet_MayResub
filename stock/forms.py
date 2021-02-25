from django import forms
from .models import Stock


class SearchForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product']


class AddStock(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['receive_qty']


class RemoveStock(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['issue_qty']
