from django.db import models




class Book(models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    publisher = models.CharField(max_length=255, blank=False, null=True)
    year = models.DateField( blank=False)
    isbn = models.CharField(max_length=255, blank=False, null=True)
    backcover = models.TextField( blank=False, null=True)
    cover = models.BooleanField( blank=False, null=True)
    pass