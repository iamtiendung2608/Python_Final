from django.shortcuts import render

# Create your views here.
'''function base view'''
'''CODE: comment functionality of each function'''
'''views to html file in template folder just using the name EX: RETURN RENDER(REQUEST,'INDEX.HTML',CONTEXT)'''

def get_store(request):
    context = {}
    return render(request, 'store.html', context)