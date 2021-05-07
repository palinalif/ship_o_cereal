from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.forms.accountForm import AccountRegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': AccountRegisterForm()
    })