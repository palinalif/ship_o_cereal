from django.forms import ModelForm, widgets
from user.models import Profile, Address

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user', 'address']
        widgets={
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'photo': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.NumberInput(attrs={'class': 'form-control'})
        }
    class Meta2:
        model = Address
        exclude = ['id']
        widgets={
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'houseNumber': widgets.NumberInput(attrs={'class': 'form-control'}),
            'streetName': widgets.TextInput(attrs={'class': 'form-control'}),
            'postNumber': widgets.NumberInput(attrs={'class': 'form-control'})
        }