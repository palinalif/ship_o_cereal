from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.forms.accountForm import AccountRegisterForm
from user.models import Profile, Address, Order
from cart.models import OrderItem
from user.forms.profile_form import ProfileForm
from cart.views import getTotalPrice
from django.contrib.auth.decorators import login_required
from error.views import *


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })

@login_required
def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            if profile is None:
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
            return redirect('profile')
    if profile is None:
        return render(request, 'user/profile.html', {
            'form': ProfileForm(instance=profile)})
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile, initial={
            'country': request.user.profile.address.country,
            'city': request.user.profile.address.city,
            'houseNumber': request.user.profile.address.houseNumber,
            'streetName': request.user.profile.address.streetName,
            'postNumber': request.user.profile.address.postNumber
        }),
        'orders': Order.objects.filter(profile=profile, status='Done')
    })

@login_required
def oldOrder(request, orderID):
    profile = Profile.objects.filter(user=request.user).first()
    order = Order.objects.filter(pk=orderID).first()
    if order is None:
        return error_404_view(request, None)
    if order.profile == profile:
        items = OrderItem.objects.filter(order=order)

        return render(request, 'user/old_order.html', {
            'dateCreated': order.dateCreated,
            'items': items,
            'totalPrice': getTotalPrice(items)
        })
    return error_403_view(request, None)
