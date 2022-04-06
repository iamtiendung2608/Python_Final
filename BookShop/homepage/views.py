from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''function base view'''
'''CODE: comment functionality of each function'''
'''views to html file in template folder just using the name EX: RETURN RENDER(REQUEST,'INDEX.HTML',CONTEXT)'''


def homepage_view(request, *args, **kwargs):
    return HttpResponse('<h1>Hello World</h1>')
