from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/
    path('', views.index, name="description-index")
]