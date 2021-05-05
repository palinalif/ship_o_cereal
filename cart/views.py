from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'cart/index.html')
def pay(request):
    return render(request, 'cart/pay.html')
def review(request):
    return render(request, 'cart/review.html')
def receipt(request):
    return render(request, 'cart/receipt.html')