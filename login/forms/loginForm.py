from django.forms import ModelForm
from login.models import User

class loginCreateForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id']
        widgets = {
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
            'password': widgets.TextInput(attrs={'class': 'form-control'}),
        }