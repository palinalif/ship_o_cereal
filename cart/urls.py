from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/cart
    path('', views.index, name="cart-index"),
    #http://localhost:8000/cart/confirm-card
    path('confirm-card/', views.pay, name="confirm-card"),
    #http://localhost:8000/cart/review
    path('review/', views.review, name="review"),
    #http://localhost:8000/cart/receipt
    path('receipt/', views.receipt, name="receipt"),

    path('addToCart/', views.addToCart, name="addToCart"),
    path('removeFromCart/', views.removeFromCart, name="removeFromCart")
]
