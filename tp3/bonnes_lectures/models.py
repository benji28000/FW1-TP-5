from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




class IsbnField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 17
        super().__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if not value.startswith('978'):
            raise ValidationError('ISBN must start with 978')

    def formfield(self, **kwargs):
        defaults = {'max_length': self.max_length}
        defaults.update(kwargs)
        return super().formfield(**defaults)

class Author(models.Model):
    nom = models.CharField(max_length=255, blank=False, null=True)
    prenom = models.CharField(max_length=255, blank=False, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors', null=True)

class Book(models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    authors = models.ManyToManyField(Author, related_name='books')
    isbn = IsbnField()
    year = models.DateField(blank=False)
    backcover = models.TextField(blank=False, null=True)
    cover = models.ImageField(upload_to='images/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', null=True)

class ISBN (models.Model):
    domaine = models.CharField(max_length=255, blank=False, null=True)
    num_editeur = models.CharField(max_length=255, blank=False, null=True)
    num_publication = models.CharField(max_length=255, blank=False, null=True)
    cle = models.CharField(max_length=255, blank=False, null=True)

    def is_valid_isbn(self):
        if isinstance(self.domaine, int):
            return False
        if isinstance(self.num_editeur, int):
            return False
        if isinstance(self.num_publication, int):
            return False
        if isinstance(self.cle, int):
            return False
        if len(self.num_publication) != 7:
            return False
        if len(self.domaine) != 3:
            return False
        if len(self.num_editeur) != 1:
            return False
        if len(self.cle) != 1:
            return False
        return True

class Review(models.Model):
    date = models.DateField(blank=False)
    text = models.TextField(blank=False, null=True)
    note = models.IntegerField(blank=False, null=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=True)

