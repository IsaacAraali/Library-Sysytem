from django import forms


class BookrequestForm(forms.Form):
    student_name = forms.CharField(max_length=255)
    student_number =forms.CharField(max_length=255)
    name = forms.CharField(max_length=255)
    author = forms.CharField(max_length=255)
    category = forms.CharField(max_length=255)
    subject = forms.CharField(max_length=255)