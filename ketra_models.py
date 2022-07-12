from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_librarian = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class librarian (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key =True)
    staff_id_number = models.CharField(max_length=10)


class student (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key =True)
    student_webmail = models.CharField(max_length=10)
    registration_number = models.CharField(max_length=10)
    student_number = models.CharField(max_length=10)

                                                                                  