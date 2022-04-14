from django.contrib import admin
from django.urls import path
from homepage import views as homepage



urlpatterns = [ 
     path('', homepage.get_Book, name ='books'),
     #path('', homepage.get_store, name ='store'),
]