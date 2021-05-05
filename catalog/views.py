from django.shortcuts import render

from products.views import getCereals, getSortedBy, getFilterBy

# Create your views here.
def index(request):
    return render(request, 'catalog/index.html', context=({'cereals': getCereals()}))

def sortedBy(request, att):
    return render(request, 'catalog/index.html', context=({'cereals': getSortedBy(att)}))

def filterBy(request, label):
    return render(request, 'catalog/index.html', context=({'cereals': getFilterBy(label)}))
