from django import forms
from .models import Stock


class SearchForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product']
