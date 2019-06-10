from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('list', views.lists, name="list"),
    path('add', views.add, name="add"),
]