from django.urls import path

from core import views

urlpatterns = [
    path('profile/<int:pk>/', views.UserDetailView.as_view()),
    path('signup/', views.UserCreateView.as_view()),
]
