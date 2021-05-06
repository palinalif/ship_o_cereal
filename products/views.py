from django.shortcuts import render, get_object_or_404
from products.models import *
from products.forms.createProduct import ProductCreateForm

# Create your views here.

def getCereals():
    return Product.objects.all()

def getSortedBy(strin):
    return sorted(cereals, key = lambda i: i[strin])

def getFilterBy(strin):
    newCereals= []
    for i in cereals:
        if i['label'] == strin.capitalize():
            newCereals.append(i)
    return newCereals

def product(request, id):
    # TODO: make id check and if invalid goto 404 page
    return render(request, 'products/index.html', {
        'cereal': get_object_or_404(Product, pk=id)
    })

def createProduct(request):
    if request.method == 'POST':
        print(1)
    else:
        form = ProductCreateForm()
    return render(request, 'products/create.html', {
        'form': form
    })