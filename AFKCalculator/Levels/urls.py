from django.contrib import admin
from django.urls import path
from Levels import views

urlpatterns = [
    path('', views.calculate_costs_view, name='calculator'),
]