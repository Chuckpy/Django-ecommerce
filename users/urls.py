from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="account/login.html"), name="login"),
    path("register/", auth_views.LoginView.as_view(template_name="account/register.html"), name="register"),
]
