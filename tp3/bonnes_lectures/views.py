from .forms import BookForm, ReviewForm, AuthorForm, InscriptionForm, LoginForm
from .models import Book, Review, Author
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


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

@login_required
def bookcreate(request):
    form = BookForm()
    if (request.method == "POST"):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
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
            'books': books,

        }
    )

def bookshow(request, id=None):
    book = Book.objects.get(id=id)
    list1_to_5 = [1, 2, 3, 4, 5]
    return render(
        request,
        "Book/show.book.html",
        {
            'book': book,
            'list1_to_5': list1_to_5
        }
    )

@login_required
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

@login_required
def bookdelete(request, id=None):
    if (request.method == "POST"):
        book = Book.objects.get(id=id)
        book.delete()
    return redirect('book_list')

@login_required
def reviewcreate(request):
    form = ReviewForm()
    if (request.method == "POST"):
        form = ReviewForm(request.POST)
        if form.is_valid():
            user = request.user
            form.instance.user = user
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

@login_required
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

@login_required
def reviewdelete(request, id=None):
    if (request.method == "POST"):
        review = Review.objects.get(id=id)
        review.delete()
    return redirect('review_list')

@login_required
def authorcreate(request):
    form = AuthorForm()
    if (request.method == "POST"):
        form = AuthorForm(request.POST)
        if form.is_valid():
            user = request.user
            form.instance.user = user
            form.save()
            return redirect('author_list')
    return render(
        request,
        "Author/create.author.html",
        {
            'form': form
        }
    )

def authorlist(request):
    authors = Author.objects.all()
    return render(
        request,
        "Author/index.author.html",
        {
            'authors': authors.values()
        }
    )

def authorshow(request, id=None):
    author = Author.objects.get(id=id)
    return render(
        request,
        "Author/show.author.html",
        {
            'author': author
        }
    )

@login_required
def authoredit(request, id=None):
    author = Author.objects.get(id=id)
    if (request.method == "POST"):
        form=AuthorForm(request.POST,instance=author)
        if(form.is_valid()):
            form.save()
            return redirect('author_show', id)
    else:
        form = AuthorForm(instance=author)

    return render(
        request,
        "Author/edit.author.html",
        {
            'form': form,
            'author': author
        }
    )

@login_required
def authordelete(request, id=None):
    if (request.method == "POST"):
        author = Author.objects.get(id=id)
        author.delete()
    return redirect('author_list')




def Inscription(request):
    form = InscriptionForm()
    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            return redirect('index')
        else:
            return render(request, "inscription.html", {'form': form})
    return render(request, "inscription.html", {'form': form})



def Login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list')
    return render(request, "login.html", {"form": form})

def Logout(request):
    logout(request)
    return redirect('login')




