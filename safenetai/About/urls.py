from django.contrib import admin
from django.urls import path
from About import views

urlpatterns = [
    path("", views.about, name='about'),
]
