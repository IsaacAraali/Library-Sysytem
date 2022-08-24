from django.db import models

# Create your models here.
class Bookrequest(models.Model):
    student_name =models.CharField(max_length=255)
    student_number = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)