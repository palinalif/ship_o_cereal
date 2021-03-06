from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from cart.forms.NewCardForm import NewCardForm
from user.forms.profile_form import ProfileForm
from user.models import PaymentInfo, Address
from error.views import *

from user.models import Profile, Order
from cart.models import OrderItem, Product

# Create your views here.

def order_item_queries_to_list(queries):
    items = []
    for item in queries:
        i = {
            "product": {
                "name": item.product.name,
                "price": item.product.price
            },
            "quantity": item.quantity,
            "order_id": item.order.id
        }
        items.append(i)
    return items

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

def getTotalPrice(orderItems):
    total = 0
    for item in orderItems:
        total += item.quantity * item.product.price
    return total

@login_required
def index(request):
    profile = Profile.objects.filter(user=request.user).first()
    if profile is None:
        return redirect('profile')
    else:
        order = Order.objects.filter(profile=profile, status='In Progress').first()
        request.session['totalPrice'] = getTotalPrice(OrderItem.objects.filter(order=order))
        return render(request, 'cart/index.html', {
            'profile': profile,
            'address': profile.address,
            'items': OrderItem.objects.filter(order=order),
            'totalPrice': request.session['totalPrice']
        })

def addToCart(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
        if profile is None:
            return JsonResponse({'amount': -1})
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
    return HttpResponseForbidden()


def removeFromCart(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
        order = Order.objects.filter(profile=profile, status='In Progress').first()
        product = Product.objects.filter(id=request.POST['id']).first()
        item = OrderItem.objects.filter(order=order, product=product).first()
        item.delete()
        request.session['totalPrice'] = getTotalPrice(OrderItem.objects.filter(order=order))
        return JsonResponse({'id': request.POST['id'], 'totalPrice': request.session['totalPrice']})

def cartEmptyCheck(request):
    order = Order.objects.filter(profile=request.user.profile, status='In Progress').first()
    if order is None:
        return error_400_view(request, None)
    product = OrderItem.objects.filter(order=order).first()
    if product is None:
        return error_400_view(request, None)

@login_required
def contactInfo(request):
    isEmpty = cartEmptyCheck(request)

    if isEmpty is not None:
        return isEmpty

    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            if profile.address is None:
                address_instance = Address()
            else:
                address_instance = request.user.profile.address
            address_instance.country = request.POST['country']
            address_instance.city = request.POST['city']
            address_instance.houseNumber = request.POST['houseNumber']
            address_instance.streetName = request.POST['streetName']
            address_instance.postNumber = request.POST['postNumber']
            address_instance.save()
            profile = form.save(commit=False)
            profile.user = request.user
            profile.address = address_instance
            profile.save()
            return redirect('confirm-card')
    if request.user.profile.address is None:
        initial = {}
    else:
        initial = {
            'country': request.user.profile.address.country,
            'city': request.user.profile.address.city,
            'houseNumber': request.user.profile.address.houseNumber,
            'streetName': request.user.profile.address.streetName,
            'postNumber': request.user.profile.address.postNumber
        }
    return render(request, 'cart/contact_info.html', {
        'form': ProfileForm(instance=profile, initial=initial),
    })

@login_required
def pay(request):
    isEmpty = cartEmptyCheck(request)

    if isEmpty is not None:
        return isEmpty

    if request.method == 'POST':
        form = NewCardForm(data=request.POST)
        if form.is_valid():
            newCard = form.save(commit=False)
            request.session['currentCard'] = {
                'cardNumber': newCard.cardNumber,
                'cardHolder': newCard.cardHolder,
                'expDate': newCard.expDate,
                'cvc': newCard.cvc,
            }
            return redirect('review')
    else:
        if 'currentCard' in request.session.keys():
            form = NewCardForm(initial=request.session['currentCard'])
        else:
            form = NewCardForm()

    return render(request, 'cart/pay.html', {
        'cardForm': form,
    })

@login_required
def review(request):
    isEmpty = cartEmptyCheck(request)

    if isEmpty is not None:
        return isEmpty

    if 'currentCard' in request.session.keys():
        profile = Profile.objects.filter(user=request.user).first()
        order = Order.objects.filter(profile=profile, status='In Progress').first()

        return render(request, 'cart/review.html', {
            'profile': profile,
            'address': profile.address,
            'items': OrderItem.objects.filter(order=order),
            'cardNumber': request.session['currentCard']['cardNumber'],
            'totalPrice': request.session['totalPrice']
        })
    return error_400_view(request, None)

@login_required
def receipt(request):
    isEmpty = cartEmptyCheck(request)

    if isEmpty is not None:
        return isEmpty

    if 'currentCard' in request.session.keys():
        user_info = construct_user_dict(request)
        order = Order.objects.filter(profile=request.user.profile, status='In Progress').first()
        order.status = 'Done'
        order.save()
        order_list = order_item_queries_to_list(OrderItem.objects.filter(order=order))
        return render(request, 'cart/receipt.html', {"user_info": user_info, "address": request.user.profile.address, "items": order_list, "basic_user_info": {'name': user_info['name']}, "totalPrice": request.session['totalPrice']})

    return error_400_view(request, None)