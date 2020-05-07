from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('notes/add', views.add_note, name='add_note'),
    path('', views.index, name='index'),
    path(r'^accounts/login/', auth_views.LoginView.as_view(), name='login'),
]