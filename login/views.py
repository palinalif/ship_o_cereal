from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
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
    #if request.method == 'POST':
    #    print(1)
    #else:
    #    print(2)
    #return render(request, '/login', {
    #    'form': form
    #})
