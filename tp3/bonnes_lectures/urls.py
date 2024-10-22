from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/',views.about,name="about"),
    path('welcome/',views.welcome,name="welcome"),
path('book/create', views.bookcreate, name="book_create"),
path('book/', views.booklist, name="book_list"),
path('book/show/<int:id>', views.bookshow, name="book_show"),
path('book/edit/<int:id>', views.bookedit, name="book_edit"),
path('book/delete/<int:id>', views.bookdelete, name="book_delete"),
]