from django.forms import ModelForm, widgets, inlineformset_factory
from user.models import Profile, Address
from django.contrib.auth.models import User
from django import forms
from django_countries.fields import CountryField


class ProfileForm(ModelForm):
    country = CountryField().formfield()
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    houseNumber = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    streetName = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    postNumber = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        exclude = ['id', 'user', 'address']
        widgets={
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'photo': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.NumberInput(attrs={'class': 'form-control'})
        }

class OnlyProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user', 'address']
        widgets={
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'photo': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.NumberInput(attrs={'class': 'form-control'})
        }