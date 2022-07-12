from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from.models import librarian,student,User
from django import forms


class librarianSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    staff_id_number = forms.CharField(required=True)


    class Meta (UserCreationForm.Meta):
        model = User


    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_librarian = True 
        user.is_staff = True 
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        librarian= librarian.objects.create(user=user)
        librarian.staff_id_number = self.cleaned_data.get('staff_id_number')
        librarian.save()
        return librarian


class studentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    student_webmail = forms.CharField(required=True)
    registration_number = forms.CharField(required=True)
    student_number = forms.CharField(required=True)

    class Meta (UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        student= student.objects.create(user=user)
        student.student_webmail = self.cleaned_data.get('student_webmail')
        student.registration_number = self.cleaned_data.get('registration_number')
        student.student_number = self.cleaned_data.get('student_number')
        student.save()
        return student


                                            