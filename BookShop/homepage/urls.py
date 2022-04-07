from django.contrib import admin
from django.urls import path
from homepage import views as homepage



urlpatterns = [ 
     path('', homepage.get_store, name ='store'),
]