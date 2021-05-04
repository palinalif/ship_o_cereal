from django.shortcuts import render

from product.views import getCereals

# Create your views here.
def index(request):
    return render(request, 'catalog/index.html', context=({'cereals': getCereals()}))