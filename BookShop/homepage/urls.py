from turtle import home
from django.contrib import admin
from django.urls import path
from homepage import views as homepage


urlpatterns = [ 
     path('', homepage.get_Book, name ='books'),
     path('tag/<int:id>',homepage.get_tag,name='tag'),
     path('edit',homepage.add_book,name='edit'),
]