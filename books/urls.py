from django.urls import path, include
from . import views





urlpatterns = [
    path('bookslist/', views.booksList),
    path('bookslist/<int:pk>/', views.booksDetails),
]