from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction


class LibSignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30)
    last_name = forms.CharField(
        max_length=30)
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')
    staff_id_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'staff_id_number', 'password1', 'password2', )

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_librarian = True
        user.is_staff = True


class StudSignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30)
    last_name = forms.CharField(
        max_length=30)
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')
    student_number = forms.CharField(required=True)
    registration_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'student_number', 'registration_number', 'password1', 'password2', )

    @transaction.atomic
    def data_save(self):
        user = super().save(commit=False)
        user.is_student = True


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(
        max_length=16, label='password', widget=forms.PasswordInput)
