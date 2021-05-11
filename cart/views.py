from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
import json
from .forms import PayForm
from .forms import NewCardForm
from user.models import Profile, Address, PaymentInfo

from cart.models import Order, OrderItem, Product
# Create your views here.

def construct_user_dict(request):
    user_info = {
        'name': request.user.profile.name,
        'email': request.user.profile.email,
        'phone': request.user.profile.phone,
        'streetName': request.user.profile.address.streetName,
        'houseNumber': request.user.profile.address.houseNumber,
        'city': request.user.profile.address.city,
        'country': request.user.profile.address.country,
        'postalCode': request.user.profile.address.postNumber
    }
    return user_info

def construct_card_dict(request):
    profile = Profile.objects.filter(user=request.user).first()
    cardQueries = PaymentInfo.objects.filter(profile=profile)
    cards = []
    for card in cardQueries:
        c = {
            'cardHolderName':card.cardHolder,
            'cardNumber':card.cardNumber,
            'expDate':card.expDate,
            'cvc':card.cvc
        }
        cards.append(c)
    return cards


@login_required
def index(request):
    user_info = construct_user_dict(request)
    return render(request, 'cart/index.html', user_info)

def addToCart(request):
    if request.user.is_authenticated:
        # Add to the database to the cart
        print(request.POST['amount'])
        return JsonResponse({'amount': request.POST['amount'], 'id': request.POST['id']})


@login_required
def pay(request):
    pay_form = PayForm(request.POST or None, initial=request.session.get('PayFormData'), request=request)
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
    return render(request, 'cart/pay.html', {"buttonForm": pay_form, "cardForm": new_card_form})


@login_required
def review(request):
    user_info = construct_user_dict(request)
    cards = construct_card_dict(request)
    try:
        if request.session['selected_card']:
            card_num = request.session['selected_card']
    except KeyError:
        card_id = request.session['selected_card_id']
        card_num = str(cards[int(card_id) - 1]["cardNumber"])
    return render(request, 'cart/review.html', {"user_info": user_info, "card_num": card_num})

@login_required
def receipt(request):
    user_info = construct_user_dict(request)
    return render(request, 'cart/receipt.html', user_info)


