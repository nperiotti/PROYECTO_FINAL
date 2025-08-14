from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, DetailView, View
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from .forms import RegisterForm, AvatarForm, ProfileUpdateForm
from .models import Avatar
from django.contrib.auth.mixins import LoginRequiredMixin

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
    next_page = reverse_lazy('home')

class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'App_LogIn/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user

class AvatarUpdateView(LoginRequiredMixin, UpdateView):
    model = Avatar
    form_class = AvatarForm
    template_name = 'App_LogIn/avatar.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        avatar, created = Avatar.objects.get_or_create(user=self.request.user)
        return avatar

class ProfileUpdateView(LoginRequiredMixin,View):
    template_name = 'App_LogIn/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get(self, request, *args, **kwargs):
        user_form = ProfileUpdateForm(instance=request.user)

        avatar, _ = Avatar.objects.get_or_create(user=request.user)
        avatar_form = AvatarForm(instance=avatar)
        password_form = PasswordChangeForm(request.user)
        context = {
            'user_form': user_form,
            'avatar_form': avatar_form,
            'password_form': password_form
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        user_form = ProfileUpdateForm(request.POST, instance=request.user)
        avatar, _ = Avatar.objects.get_or_create(user=request.user)
        avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        password_form = PasswordChangeForm(request.user, request.POST)

        if "update_profile" in request.POST:
            if user_form.is_valid() and avatar_form.is_valid():
                user_form.save()
                avatar_form.save()
                return redirect(self.success_url)
        elif "change_password" in request.POST:
            
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                return redirect(self.success_url)

        context = {
            'user_form': user_form,
            'avatar_form': avatar_form,
            'password_form': password_form
        }
        return render(request, self.template_name, context)