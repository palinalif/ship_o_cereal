from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.models import Profile, Address, SearchHistory
from user.models import Profile, Address, Order
from cart.models import OrderItem
from user.forms.profile_form import OnlyProfileForm
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

def aboutUs(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/aboutUs.html')

def seeSearchHistory(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/seeSearchHistory.html', {
        'searchHistory': SearchHistory.objects.filter(profile=request.user.profile)
    })

@login_required
def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = OnlyProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    if profile is None:
        return render(request, 'user/profile.html', {
            'form': OnlyProfileForm()
        })
    return render(request, 'user/profile.html', {
        'form': OnlyProfileForm(instance=profile),
        'orders': Order.objects.filter(profile=profile, status='Done').order_by('-dateCreated')
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
