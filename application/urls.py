from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('notes/add/', views.add_note, name='add_note'),
    path('notes/edit/<str:note_id>', views.edit_note, name='edit_note'),
    path('notes/delete/<str:note_id>', views.delete_note, name='delete_note'),
    path('notes/update/<str:pk>', views.update_note, name='update_note'),
    path('', views.index, name='index'),
]