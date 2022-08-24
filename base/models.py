from email.policy import default
from django.db import models

# Create your models here.


class Book(models.Model):
    book_id = models.CharField(max_length=10, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name + ' ' + self.author + ' ' + self.description


class BorrowedBook(models.Model):
    book_id = models.CharField(max_length=10)
    book_name = models.CharField(max_length=50)
    date_borrowed = models.DateTimeField(auto_now_add=True)
    date_return = models.DateTimeField(blank=False)
    std_id = models.CharField(max_length=10)
    std_name = models.CharField(max_length=50)

    def __str__(self):
        return self.book_id + ' ' + self.book_name + ' ' + str(self.date_borrowed) + ' ' + str(self.date_return) + ' ' + self.std_id + ' ' + self.std_name

def get_expiry():
    return datetime.today() + timedelta(days=5)

class IssueBook(models.Model):
    student_name = models.CharField(max_length=225)
    student_number = models.IntegerField()
    name = models.CharField(max_length=223)
    isbn = models.IntegerField()
    author = models.CharField(max_length=225)
    category = models.CharField(max_length=225)
    subject_area = models.CharField(max_length=20)
    issue_date = models.DateTimeField(auto_now=True)
    expiry_date = models.DateTimeField(default=get_expiry)

    def __str__(self):
        return self.student_name + ' ' + self.name + ' ' + ' ' + self.issue_date
