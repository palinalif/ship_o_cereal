from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

cart = {}

def index(request):
    return render(request, 'cart/index.html')

def pay(request):
    return render(request, 'cart/pay.html')

def review(request):
    return render(request, 'cart/review.html')
def receipt(request):
    return render(request, 'cart/receipt.html')

def addToCart(request):
    if request.method == 'POST':
        print(1)
    else:
        print(2)
    # if cereal not in cart.keys():
    #     cart[cereal] = amount
    # else:
    #     cart[cereal] += amount
    return re
