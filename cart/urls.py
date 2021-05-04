from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/cart
    path('', views.index, name="cart-index"),
    #http://localhost:8000/cart/confirm-card
    path('confirm-card/', views.pay, name="confirm-card")
]
