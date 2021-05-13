from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from cart.forms.NewCardForm import NewCardForm
from user.models import PaymentInfo

from user.models import Profile, Order
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
    if request.method == 'POST':
        if 'cardID' in request.POST:
            request.session['cardID'] = int(request.POST['cardID'])
        form = NewCardForm(data = request.POST)
        if form.is_valid():
            newCard = form.save(commit=False)
            newCard.profile = Profile.objects.filter(user=request.user).first()
            newCard.save()
            request.session['cardID'] = newCard.id
            return redirect('review')
    else:
        form = NewCardForm()

    return render(request, 'cart/pay.html', {
        'cardForm': form,
        'cards': cards,
    })

@login_required
def review(request):
    profile = Profile.objects.filter(user=request.user).first()
    order = Order.objects.filter(profile=profile, status='In Progress').first()
    cards = PaymentInfo.objects.filter(profile=profile)
    cardNumber = cards.filter(pk=request.session['cardID']).first().cardNumber

    return render(request, 'cart/review.html', {
        'profile': profile,
        'address': profile.address,
        'items': OrderItem.objects.filter(order=order),
        'cardNumber': cardNumber,
        'totalPrice': request.session['totalPrice']
    })

@login_required
def receipt(request):
    return render(request, 'cart/receipt.html', {'address': request.user.profile.address})