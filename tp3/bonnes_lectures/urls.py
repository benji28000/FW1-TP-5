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
path('review/create', views.reviewcreate, name="review_create"),
path('review/', views.reviewlist, name="review_list"),
path('review/show/<int:id>', views.reviewshow, name="review_show"),
path('review/edit/<int:id>', views.reviewedit, name="review_edit"),
path('review/delete/<int:id>', views.reviewdelete, name="review_delete"),
]