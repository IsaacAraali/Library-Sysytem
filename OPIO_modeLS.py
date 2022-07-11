from django.db import models


class AvailableBooks(models.Model):
    book_name = models.CharField(max_length=250)
    isbn = models.IntegerField()
    author = models.CharField(max_length=250)
    image_url = models.CharField(max_length=2083)
    category = models.CharField(max_length=20)
    subject_area = models.CharField(max_length=20)


class BooksNotReturned(models.Model):
    book_name = models.CharField(max_length=250)
    isbn = models.IntegerField()
    author = models.CharField(max_length=250)
    category = models.CharField(max_length=20)
    subject_area = models.CharField(max_length=20)
    image_url = models.CharField(max_length=2083)


