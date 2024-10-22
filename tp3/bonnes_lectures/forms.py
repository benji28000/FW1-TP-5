from .models import Book
from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publisher', 'year', 'isbn', 'backcover', 'cover']
        widgets = {
            'year': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
