from django import forms
from dataclasses import fields
from .models import Book


class BooksForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'image', 'description']
