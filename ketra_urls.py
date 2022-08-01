from django.urls import path
from .import views
from django.contrib import admin
from login.views import librarian_register

urlpatterns=[
    path('register/',views.register,name='register'),
    path('librarian_register/',views.librarian_register.as_view(),name='librarian_register'),
    path('student_register/',views.student_register.as_view(),name='student_register'),
]





