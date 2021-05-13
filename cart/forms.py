from django import forms
from django.forms import widgets, ModelForm
from django.utils.safestring import mark_safe
from user.models import Profile, Address, PaymentInfo

class NewCardForm(ModelForm):
    class Meta:
        model = PaymentInfo
        exclude = ['id', 'profile']
        widgets = {
            'cardHolder': widgets.TextInput(attrs={'class': 'form-control'}),
            'cardNumber': widgets.TextInput(attrs={'class': 'form-control'}),
            'expDate': widgets.TextInput(attrs={'class': 'form-control'}),
            'cvc': widgets.TextInput(attrs={'class': 'form-control'})
        }