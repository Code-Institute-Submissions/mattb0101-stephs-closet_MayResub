from django import forms
from products.models import Product, Category, Sub_Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        cat_friendlynames = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = cat_friendlynames
        for field_name, field in self.fields.items():
