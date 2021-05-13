from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
import json
from .forms import NewCardForm
from user.models import Profile, Address, PaymentInfo

from user.models import Profile, Order, Address
from cart.models import OrderItem, Product
# Create your views here.

def updateTotalPrice(request, orderItems):
    total = 0
    for item in orderItems:
        total += item.quantity * item.product.price
    request.session['totalPrice'] = total

@login_required
def index(request):
    profile = Profile.objects.filter(user=request.user).first()
    order = Order.objects.filter(profile=profile, status='In Progress').first()
    updateTotalPrice(request, OrderItem.objects.filter(order=order))
    return render(request, 'cart/index.html', {
        'profile': profile,
        'address': profile.address,
        'items': OrderItem.objects.filter(order=order),
        'totalPrice': request.session['totalPrice']
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
        updateTotalPrice(request, OrderItem.objects.filter(order=order))
        return JsonResponse({'id': request.POST['id'], 'totalPrice': request.session['totalPrice']})

@login_required
def pay(request):
    cards = PaymentInfo.objects.filter(profile=request.user.profile)

    newCard = PaymentInfo()
    newCardForm = NewCardForm()
    if request.method == 'POST':
        newCardForm = NewCardForm(data=request.POST)
        if 'cardID' in request.POST:
            request.session['selectedCard'] = cards.filter(pk=request.POST['cardID'])
            print("use")
        elif newCardForm.is_valid():
            # To save the fact that you chose new card
            # request.session['PayFormData'] = pay_form.cleaned_data
            # process data, save in session
            newCard = newCardForm.save(commit=False)
            newCard.profile = request.user.profile
            newCard.save()
            # Saves the card number in session to be used on the next page
            request.session['selectedCard'] = newCard
            print("new")
    return render(request, 'cart/pay.html', {"cards": cards, "cardForm": newCardForm})


@login_required
def review(request):
    print("hello")
    profile = Profile.objects.filter(user=request.user).first()
    order = Order.objects.filter(profile=profile, status='In Progress').first()
    cards = PaymentInfo.objects.filter(profile=profile)
    request.session['selectedCard'] = 12
    cardNum = cards.filter(pk=request.session['selectedCard']).first().cardNumber

    return render(request, 'cart/review.html', {
        'profile': profile,
        'address': profile.address,
        'items': OrderItem.objects.filter(order=order),
        'cardNum': cardNum,
        'totalPrice': request.session['totalPrice']
    })

@login_required
def receipt(request):
    user_info = construct_user_dict(request)
    return render(request, 'cart/receipt.html', user_info)


