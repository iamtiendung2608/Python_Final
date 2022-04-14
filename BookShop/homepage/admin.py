from django.contrib import admin
from .models import Book, Tag

# Register your models here.
'''import model and add it to admin site'''
admin.site.register(Book)
admin.site.register(Tag)
