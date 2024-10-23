from django import forms
from .models import Book

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
