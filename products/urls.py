from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/
    path('<int:id>/', views.product, name="product-index"),
    path('create/', views.createProduct, name="create-product"),
    path('delete/<int:id>', views.deleteProduct, name="delete-product")
]