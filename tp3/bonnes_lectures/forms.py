from django import forms
from .models import Book, Review, Author
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'year', 'isbn', 'backcover', 'cover']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'authors': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'year': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the ISBN'}),
            'backcover': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter the back cover description'}),
            'cover': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['date', 'text', 'note', 'book']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter the review'}),
            'note': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the note'}),
            'book': forms.Select(attrs={'class': 'form-control'}),
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['nom', 'prenom']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the last name'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the first name'}),
        }

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter the email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter the password'}),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter the password'}),
        }