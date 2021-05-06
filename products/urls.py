from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/
    path('<int:id>/', views.product, name="products-index"),
    path('create/', views.createProduct, name="create-product")
]