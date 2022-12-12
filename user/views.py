from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView


class Login(LoginView):
    template_name = "user/login.html"


class Logout(LogoutView):
    success_url = ""


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = "user/register.html"
    success_url = "/chamber/"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("/chamber/")
        return super().get(request, *args, **kwargs)
