from django.contrib import admin
from .models import User,librarian,student

# Register your models here.
admin.site.register(User)
admin.site.register(librarian)
admin.site.register(student)