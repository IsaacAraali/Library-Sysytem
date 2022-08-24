from django import forms
from dataclasses import fields
from .models import Book


class BooksForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'image', 'description']


class IssueBookForm(forms.Form):
    student_name = forms.CharField(max_length=225)
    student_number = forms.IntegerField()
    name = forms.CharField(max_length=223)
    isbn = forms.IntegerField()
    author = forms.CharField(max_length=225)
    category = forms.CharField(max_length=225)
    subject_area = forms.CharField(max_length=20)
    
