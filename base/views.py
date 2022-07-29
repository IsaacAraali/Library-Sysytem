from django.shortcuts import render, redirect
from .models import Book
from .book_form import BooksForm
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'base/index.html')


def books(request):
    all = Book.objects.all
    context = {'book': all}
    return render(request, 'base/books.html', context)


def add_books(request):
    if request.method == 'POST' or None:
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('available_books')
    else:
        form = BooksForm()
        return render(request, 'base/add_book.html', {'form': form})
    form = BooksForm()


def my_book(request, pk):
    books = Book.objects.filter(pk=pk)
    return render(request, 'base/my_book.html', {'book': books})


def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    form = BooksForm(instance=book)
    if request.method == 'POST' or None:
        form = BooksForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('available_books')
    else:
        form = BooksForm(instance=book)
        return render(request, 'base/add_book.html', {'form': form})


def delete_book(request, pk):
    books = Book.objects.get(pk=pk)
    if request.method == 'POST':
        books.delete()
        return redirect('available_books')
    return render(request, 'base/delete.html', {'obj': books})


def search_book(request):
    if request.method == "POST":
        searched = request.POST['searched']
        books = Book.objects.filter(name__contains=searched)
        return render(request, 'base/search.html', {'searched': searched, 'books': books})
