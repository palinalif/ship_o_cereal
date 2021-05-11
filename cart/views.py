from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
import json
from .forms import PayForm
from .forms import NewCardForm

from user.models import Profile, Order, Address
from cart.models import OrderItem, Product
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
    profile = Profile.objects.filter(user=request.user).first()
    order = Order.objects.filter(profile=profile, status='In Progress').first()
    return render(request, 'cart/index.html', {
        'profile': profile,
        'address': profile.address,
        'items': OrderItem.objects.filter(order=order)
    })

def addToCart(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
        order = Order.objects.filter(profile=profile, status='In Progress').first()
        if order is None:
            order = Order()
            order.profile = profile
            order.status = 'In Progress'
        product = Product.objects.filter(id=request.POST['id']).first()
        item = OrderItem.objects.filter(order=order, product=product).first()
        if item is None:
            item = OrderItem()
            item.product = product
            item.quantity = int(request.POST['amount'])
            item.order = order
        else:
            item.quantity += int(request.POST['amount'])
        order.save()
        item.save()
        return JsonResponse({'amount': item.quantity, 'id': request.POST['id']})

def removeFromCart(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
        order = Order.objects.filter(profile=profile, status='In Progress').first()
        product = Product.objects.filter(id=request.POST['id']).first()
        item = OrderItem.objects.filter(order=order, product=product).first()
        item.delete()
        return JsonResponse({'id': request.POST['id']})

@login_required
def pay(request):
    pay_form = PayForm(request.POST or None, initial=request.session.get('PayFormData'))
    if request.method == 'POST':
        if pay_form.is_valid():
            try:
                del request.session['selected_card']
                del request.session['selected_card_id']
            except KeyError:
                pass
            request.session['selected_card_id'] = str(request.POST['card_select'])[4:]
            #process data, save in session
            request.session.save()
            request.session['PayFormData'] = pay_form.cleaned_data
            return HttpResponseRedirect(reverse('review'))

    new_card_form = NewCardForm(request.POST or None, initial=request.session.get('NewCardFormData'))
    if request.method == 'POST':
        if new_card_form.is_valid():
            try:
                del request.session['selected_card']
                del request.session['selected_card_id']
            except KeyError:
                pass
            # To save the fact that you chose new card
            request.session['PayFormData'] = pay_form.cleaned_data
            # process data, save in session
            request.session.save()
            # Saves the card number in session to be used on the next page
            request.session['selected_card'] = request.POST['card_number']
            # saves the new card form in session
            request.session['NewCardFormData'] = new_card_form.cleaned_data
            return HttpResponseRedirect(reverse('review'))
    return render(request, 'cart/pay.html', {"cards": cards, "buttonForm": pay_form, "cardForm": new_card_form})


@login_required
def review(request):
    try:
        if request.session['selected_card']:
            card_num = request.session['selected_card']
    except KeyError:
        card_id = request.session['selected_card_id']
        card_num = str(cards[int(card_id) - 1]["cardNumber"])
    return render(request, 'cart/review.html', {"user_info": user_info, "card_num": card_num})

@login_required
def receipt(request):
    return render(request, 'cart/receipt.html', user_info)


