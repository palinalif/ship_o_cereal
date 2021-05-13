from django.shortcuts import render

# Create your views here.
def error_400_view(request, exception):
    return render(request, '400.html')

def error_403_view(request, exception):
    return render(request, '403.html')

def error_404_view(request, exception):
    return render(request, '404.html')

def error_500_view(request):
    return render(request, '500.html')