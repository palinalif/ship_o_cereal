from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/
    path('', views.index, name="index"),
    path('filter/<str:label>', views.filterBy, name="filter/name"),
    path('sort/<str:att>', views.sortedBy, name="filter/name")
]
