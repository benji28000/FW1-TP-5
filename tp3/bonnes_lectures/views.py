from .forms import BookForm, ReviewForm
from .models import Book, Review

from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(
        request,
        "index.html",
        {
            'view_name': "bonnes_lectures_view"
        }
    )

def about(request):
    return render(
        request,
        "about.html",
        {
            'view_name': "about_view"
        }
    )

def welcome(request):
    return render(
        request,
        "welcome.html",
        {
            'view_name': "welcome_view"
        }
    )

def bookcreate(request):
    form = BookForm()
    if (request.method == "POST"):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    return render(
        request,
        "Book/create.book.html",
        {
            'form': form
        }
    )

def booklist(request):
    books = Book.objects.all()
    return render(
        request,
        "Book/index.book.html",
        {
            'books': books.values()
        }
    )

def bookshow(request, id=None):
    book = Book.objects.get(id=id)
    return render(
        request,
        "Book/show.book.html",
        {
            'book': book
        }
    )

def bookedit(request, id=None):
    book = Book.objects.get(id=id)
    if (request.method == "POST"):
        form=BookForm(request.POST,instance=book)
        if(form.is_valid()):
            form.save()
            return redirect('book_show', id)
    else:
        form = BookForm(instance=book)

    return render(
        request,
        "Book/edit.book.html",
        {
            'form': form,
            'book': book
        }
    )

def bookdelete(request, id=None):
    if (request.method == "POST"):
        book = Book.objects.get(id=id)
        book.delete()
    return redirect('book_list')

def reviewcreate(request):
    form = ReviewForm()
    if (request.method == "POST"):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    return render(
        request,
        "Reviews/create.review.html",
        {
            'form': form
        }
    )

def reviewlist(request):
    reviews = Review.objects.all()
    return render(
        request,
        "Reviews/index.review.html",
        {
            'reviews': reviews.values()
        }
    )

def reviewshow(request, id=None):
    review = Review.objects.get(id=id)
    return render(
        request,
        "Reviews/show.review.html",
        {
            'review': review
        }
    )

def reviewedit(request, id=None):
    review = Review.objects.get(id=id)
    if (request.method == "POST"):
        form=ReviewForm(request.POST,instance=review)
        if(form.is_valid()):
            form.save()
            return redirect('review_show', id)
    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        "Reviews/edit.review.html",
        {
            'form': form,
            'review': review
        }
    )

def reviewdelete(request, id=None):
    if (request.method == "POST"):
        review = Review.objects.get(id=id)
        review.delete()
    return redirect('review_list')



