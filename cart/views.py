from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from cart.models import Order, OrderItem, Product
# Create your views here.

#Let's say that we already have the user that's logged in with this dictionary
user_info = {
    'id': 1,
    'name': 'Test user',
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
        'cardHolderName':'Test user',
        'cardNumber':377337278995056,
        'expDate':"0122",
        'cvc':123
    },
    {
        'userId':1,
        'cardHolderName':'Test user',
        'cardNumber':342935602344123,
        'expDate':"1125",
        'cvc':456
    }
]

@login_required
def index(request):
    if 'amount' in request.POST:
        cereal = request.POST['id']
        amount = request.POST['amount']
        return JsonResponse({'data': 123})




    return render(request, 'cart/index.html', user_info )

@login_required
def pay(request):
    return render(request, 'cart/pay.html', { "cards": cards } )

@login_required
def review(request):
    return render(request, 'cart/review.html', user_info)

@login_required
def receipt(request):
    return render(request, 'cart/receipt.html', user_info)


