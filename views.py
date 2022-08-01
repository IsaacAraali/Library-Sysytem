from django.shortcuts import render
from django.views.generic import CreateView
from .models import User,librarian,student
from .form import librarianSignUpForm,studentSignUpForm



# Create your views here.
def register(request):
        return render(request, '../templates/register.html')


class librarian_register(CreateView):
        model = User
        form_class = librarianSignUpForm
        template_name = '../templates/registration/librarian_register.html'

        
        
        
class student_register(CreateView):
        model = User
        form_class = studentSignUpForm
        template_name = '../templates/registration/student_register.html'





