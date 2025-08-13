from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("avatar/", views.AvatarUpdateView.as_view(), name="avatar"),
    path("edit_profile/", views.ProfileUpdateView.as_view(), name="edit_profile"),

]

