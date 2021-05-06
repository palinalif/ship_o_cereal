from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.

cart = {}

#Let's say that we already have the user that's logged in with this dictionary
user_info = {
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
}

#and let's say that these are their cards
cards = [
    {
        'userId':1,
        'cardHolderName':'Test User',
        'cardNumber':377337278995056,
        'expDate':"0122",
        'cvc':123
    },
    {
        'userId':1,
        'cardHolderName':'Test User',
        'cardNumber':342935602344123,
        'expDate':"1125",
        'cvc':456
    }
]

def index(request):
    return render(request, 'cart/index.html', user_info )

def pay(request):
    return render(request, 'cart/pay.html', { "cards": cards } )

def review(request):
    return render(request, 'cart/review.html', user_info)
def receipt(request):
    return render(request, 'cart/receipt.html', user_info)


