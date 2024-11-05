from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publisher', 'year', 'isbn', 'backcover', 'cover']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'publisher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the publisher'}),
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
