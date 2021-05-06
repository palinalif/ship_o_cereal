from django.shortcuts import render
from products.models import *

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
    return render(request, 'products/index.html', context=({'cereal': getCereals().get(id=id)}))