from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register', views.lib_register, name='register1'),
    path('login', views.login_user, name='login'),
    path('logout', LogoutView.as_view(
        template_name='accounts/logout.html'), name='logout'),
]
