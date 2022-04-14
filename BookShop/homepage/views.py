from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Book, Tag
from .forms import BookForm
# Create your views here.
'''function base view'''
'''CODE: comment functionality of each function'''
'''views to html file in template folder just using the name EX: RETURN RENDER(REQUEST,'INDEX.HTML',CONTEXT)'''
'''
def get_store(request):
    context = {}
    return render(request, 'store.html', context)
'''
def get_Book(request):
    q = request.GET.get('text',None)
    Items = []
    if q is None or q is '':
        Items = Book.objects.all()
    elif q is not None:
        Items = Book.objects.filter(name__contains = q)
    return render(request,'store.html',{'books':Items})
def get_tag(request,id = None):
    Items = []
    Items = Book.objects.filter(tag__ID = id)
    return render(request,'store.html',{'books':Items})

def add_book(request):
    if request.method == 'POST' :
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = BookForm()
    return render(request, 'edit.html',{'form':form})

