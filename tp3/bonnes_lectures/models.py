from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Book(models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    publisher = models.CharField(max_length=255, blank=False, null=True)
    year = models.DateField(blank=False)
    isbn = models.CharField(max_length=255, blank=False, null=True)
    backcover = models.TextField(blank=False, null=True)
    cover = models.ImageField(upload_to='images/', blank=True, null=True)

class Review(models.Model):
    date = models.DateField(blank=False)
    text = models.TextField(blank=False, null=True)
    note = models.IntegerField(blank=False, null=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
