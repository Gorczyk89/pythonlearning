from django import forms

class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=150, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)