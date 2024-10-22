from .models import Book
from .forms import BookForm
from .models import Book
from .forms import BookForm
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
        form = BookForm(request.POST)
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