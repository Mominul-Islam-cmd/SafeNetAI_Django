from django.contrib import admin
from django.urls import path
from About import views

app_name = 'About'
urlpatterns = [
    path("about_us/", views.about_us, name='about_us'),
    path("", views.index, name='index'),
   
]
