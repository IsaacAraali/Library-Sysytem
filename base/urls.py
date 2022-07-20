from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('available_books', views.books, name='available_books'),
    path('add_book', views.add_books, name='add_book'),
    path('books/<str:pk>', views.my_book, name='book')

]
