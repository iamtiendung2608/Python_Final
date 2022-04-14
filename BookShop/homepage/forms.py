from django import forms
from django.forms import ModelForm
from .models import Book, Tag
class BookForm(ModelForm):
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'class':'form-control'}))
    price = forms.CharField(label='price', widget=forms.TextInput(attrs={'class':'form-control'}))
    image = forms.CharField(label='image', widget=forms.Textarea(attrs={'class':'form-control'}))
    author = forms.CharField(label='price', widget=forms.TextInput(attrs={'class':'form-control'}))
    descript = forms.CharField(label='image', widget=forms.Textarea(attrs={'class':'form-control'}))
    tag = forms.ModelMultipleChoiceField(label='tag',queryset=Tag.objects.all())
    class Meta:
        model = Book
        fields = ['name','price','image','tag']   