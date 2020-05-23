from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('notes/add/', views.add_note, name='add_note'),
    path('notes/update/<str:pk>', views.update_note, name='update_note'),
    path('', views.index, name='index'),
]