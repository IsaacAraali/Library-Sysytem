from django.shortcuts import render, redirect
from base.models import Book

# Create your views here.


def borrow_books(request):
    title = 'request Book'
    form = BookrequestForm(request.POST)

    if form.is_valid():
        student_name = form.cleaned_data['student_name']
        student_number = form.cleaned_data['student_number']
        name = form.cleaned_data['name']
        author = form.cleaned_data['author']
        category = form.cleaned_data['category']
        subject = form.cleaned_data['subject']

        r = Bookrequest(student_name=student_name, student_number=student_number, name=name,  author=author,
                      category=category, subject=subject
                      )
        r.save()
        messages.success(request, 'Request was successfully sent')
        return redirect('book_list')
    context = {'title': title,
                   'form': form,
                   }
    return render(request, 'request.html', context)



def book_list(request):
    all = Book.objects.all
    context = {'book': all}
    return render(request, 'student/book_list.html', context)


def one_book(request, pk):
    books = Book.objects.filter(pk=pk)
    return render(request, 'student/one_book.html', {'book': books})


def search_book(request):
    if request.method == "POST":
        searched = request.POST['searched']
        books = Book.objects.filter(name__contains=searched)
        return render(request, 'student/search.html', {'searched': searched, 'books': books})

