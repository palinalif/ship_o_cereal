from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from django.shortcuts import render, redirect
from user.forms.accountForm import AccountRegisterForm
=======

>>>>>>> origin/master

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