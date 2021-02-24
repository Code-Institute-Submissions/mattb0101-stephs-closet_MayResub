from django import forms


class EmailForm(forms.Form):
    contact_name = forms.CharField(
        label="Full Name", max_length=80, required=True)
    message = forms.CharField(widget=forms.Textarea)
    contact_email = forms.EmailField(required=True)
