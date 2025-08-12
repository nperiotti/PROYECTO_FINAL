from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, update_session_auth_hash
from .forms import RegisterForm

class UserRegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'App_LogIn/register.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
        if user: 
            login(self.request, user)
        return response

class UserLoginView(LoginView):
    template_name = 'App_LogIn/login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('Proyecto_Gestion_Logistica/home')
