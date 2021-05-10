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
        'form': UserCreationForm()
    })

def index(request):
    return render(request, 'login/login.html')

def loginUser(request):
    #https://www.smashingmagazine.com/2020/02/django-highlights-user-models-authentication/
    if request.user.is_authenticated:
        return render(request, 'catalog/login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'login/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login/login.html', {'form': form})