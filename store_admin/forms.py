from django import forms
from crispy_forms.helper import FormHelper
from products.models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-3 offset-1 col-md-2 offset-md-2'
        self.helper.field_class = 'col-8 col-md-6'

        categories = Category.objects.all()
        cat_friendlynames = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = cat_friendlynames
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-0'
