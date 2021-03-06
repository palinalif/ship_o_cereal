from django import forms
from django.forms import ModelForm, widgets
from products.models import Product

class ProductForm(ModelForm):
    image = forms.CharField(required = True, widget = forms.TextInput(attrs = {'class': 'form-control'}))
    class Meta:
        model = Product
        exclude = ['id', 'nutriInfo']
        widgets = {
            'name': widgets.TextInput(attrs = {'class': 'form-control'}),
            'manufacturer': widgets.Select(attrs = {'class': 'form-control'}),
            'price': widgets.NumberInput(attrs = {'class': 'form-control'}),
            'description': widgets.TextInput(attrs = {'class': 'form-control'}),
            'amount': widgets.NumberInput(attrs = {'class': 'form-control'}),
            'tag': widgets.Select(attrs = {'class': 'form-control'}),
        }