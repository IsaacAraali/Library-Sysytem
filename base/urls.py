from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('available_books', views.books, name='available_books'),
    path('add_book', views.add_books, name='add_book'),
    path('books/<str:pk>', views.my_book, name='book'),
    path('books/update_book/<str:pk>', views.update_book, name='update_book'),
    path('books/delete_book/<str:pk>', views.delete_book, name='delete_book'),
    path('search_book', views.search_book, name='search_book'),
]
