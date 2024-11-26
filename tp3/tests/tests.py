from django.test import TestCase
from bonnes_lectures.models import Book, Author, Review,ISBN
from django.contrib.auth.models import User


class IsbnTest(TestCase):
    def test_valid_isbn(self):
        isbn = ISBN(domaine='978', num_editeur='2', num_publication='1234567', cle='8')
        self.assertTrue(isbn.is_valid_isbn())

    def test_invalid_isbn(self):
        isbn = ISBN(domaine='978', num_editeur='2', num=1234567, cle='9')
        self.assertFalse(isbn.is_valid_isbn())
        