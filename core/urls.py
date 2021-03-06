from django.urls import path

from core import views

urlpatterns = [
    path('profile', views.ProfileView.as_view()),
    path('signup', views.UserCreateView.as_view()),
    path('login', views.LoginView.as_view()),
    path('update_password', views.UserUpdatePassView.as_view()),
]
