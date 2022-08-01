from django.urls import path
from . import views

urlpatterns = [
    path('book_list', views.book_list, name='book_list'),
    path('borrowed_books', views.borrowed_books, name='borrowed_books'),
    path('books/<str:pk>', views.one_book, name='book'),
    path('search_book', views.search_book, name='search_book1'),

]
