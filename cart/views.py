from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

cart = {}

user_info = [{
    'id': 1,
    'name': 'Test User',
    'email': 'user@testuser.com',
    'phone': '123-4567',
    'password': 'dfjajfauwr89428934d',
    'streetName': 'Eitthvaðstræti',
    'houseNumber': '69',
    'city': 'Reykjavík',
    'country': 'Iceland',
    'postalCode': 109
}]

cards = [
    {
        'userId':1,
        'cardHolderName':'Test User',
        'cardNumber':377337278995056,
        'expDate':1204,
        'cvc':123
    },
    {
        'userId':1,
        'cardHolderName':'Test User',
        'cardNumber':342935602344123,
        'expDate':2408,
        'cvc':456
    }
]



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
