from django.forms import ModelForm, widgets
from django import forms
from user.models import User

class AccountRegisterForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id']
        widgets = {
            'email': widgets.TextInput(attrs = {'class': 'form-control'}),
            'password': widgets.PasswordInput(attrs = {'class': 'form-control'}),
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'photo': widgets.FileInput(attrs={'class': 'form-control'}),
            'streetName': widgets.TextInput(attrs = {'class': 'form-control'}),
            'houseNumber': widgets.TextInput(attrs = {'class': 'form-control'}),
            'postNumber': widgets.TextInput(attrs = {'class': 'form-control'}),
            'city': widgets.TextInput(attrs = {'class': 'form-control'}),
            'country': widgets.Select(attrs = {'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
        }