from django.urls import path
from .views import book_update_view, book_delete_view


path('book-update-view/<str:pk>', book_update_view, name="book-update-view"),
path('book-delete-view/<str:pk>', book_delete_view, name="book-delete-view"),