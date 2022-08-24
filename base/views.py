from django.shortcuts import render, redirect
from .models import Book, IssueBook
from student.models import Bookrequest
from .book_form import BooksForm, IssueBookForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'base/index.html')


@login_required(login_url='login')
def books(request):
    all = Book.objects.all
    context = {'book': all}
    return render(request, 'base/books.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def my_book(request, pk):
    books = Book.objects.filter(pk=pk)
    return render(request, 'base/my_book.html', {'book': books})


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
def issuing(request):
    title = 'Issue Book'
    form = IssueBookForm(request.POST or None)

    if form.is_valid():
        student_name = form.cleaned_data['student_name']
        student_number = form.cleaned_data['student_number']
        name = form.cleaned_data['name']
        isbn = form.cleaned_data['isbn']
        author = form.cleaned_data['author']
        category = form.cleaned_data['category']
        subject = form.cleaned_data['subject_area']

        p = IssueBook(student_name=student_name, student_number=student_number, name=name, isbn=isbn, author=author,
                      category=category, subject_area=subject
                      )
        p.save()
        messages.success(request, "book issued successfully")
        return redirect('available_books')
    context = {'title': title,
               'form': form,
               }
    return render(request, 'base/issuing.html', context)


@login_required(login_url='login')
def issued(request):
    title = 'All Issued  books'
    queryset = IssueBook.objects.all()

    context = {'title': title,
               'queryset': queryset,

               }

    return render(request, 'base/issued.html', context)


@login_required(login_url='login')
def requests(request):
    title = 'All requested  books'
    queryset = Bookrequest.objects.all()

    context = {'title': title,
               'queryset': queryset,

               }

    return render(request, 'base/requested.html', context)
