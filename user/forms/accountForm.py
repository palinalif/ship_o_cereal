from django.forms import ModelForm, widgets
from user.models import User

class AccountRegisterForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id']
        widgets = {
            'email': widgets.TextInput(attrs = {'class': 'form-control'}),
            'password': widgets.TextInput(attrs = {'class': 'form-control'}),
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'photo': widgets.TextInput(attrs={'class': 'form-control'}),
            'streetName': widgets.TextInput(attrs = {'class': 'form-control'}),
            'houseNumber': widgets.TextInput(attrs = {'class': 'form-control'}),
            'postNumber': widgets.TextInput(attrs = {'class': 'form-control'}),
            'city': widgets.TextInput(attrs = {'class': 'form-control'}),
            'country': widgets.TextInput(attrs = {'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
        }