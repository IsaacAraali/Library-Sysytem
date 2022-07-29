from django.shortcuts import render
from base.models import Book

# Create your views here.


def borrowed_books(request):

    return 0


def book_list(request):
    all = Book.objects.all
    context = {'book': all}
    return render(request, 'student/book_list.html', context)


def one_book(request, pk):
    books = Book.objects.filter(pk=pk)
    return render(request, 'student/one_book.html', {'book': books})
