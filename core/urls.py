from django.urls import path

from core import views

urlpatterns = [
    path('profile/<int:pk>', views.UserDetailView.as_view()),
    path('signup', views.UserCreateView.as_view()),
    path('login', views.UserLoginView.as_view()),
    path('update_password', views.UserUpdatePassView.as_view()),
    path('login', views.UserLoginView.as_view()),
]
