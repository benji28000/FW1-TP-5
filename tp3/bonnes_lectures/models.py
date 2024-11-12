from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    publisher = models.CharField(max_length=255, blank=False, null=True)
    year = models.DateField(blank=False)
    isbn = models.CharField(max_length=255, blank=False, null=True)
    backcover = models.TextField(blank=False, null=True)
    cover = models.ImageField(upload_to='images/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', null=True)

class Review(models.Model):
    date = models.DateField(blank=False)
    text = models.TextField(blank=False, null=True)
    note = models.IntegerField(blank=False, null=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=True)

class Author(models.Model):
    nom = models.CharField(max_length=255, blank=False, null=True)
    prenom = models.CharField(max_length=255, blank=False, null=True)
    books = models.ManyToManyField(Book, related_name='authors')
    reviews = models.ManyToManyField(Review, related_name='authors')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors', null=True)

