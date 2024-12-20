from django.test import TestCase
from .models import ISBN

class IsbnTest(TestCase):
    def test_valid_isbn(self):
        isbn = ISBN(domaine='978', num_editeur='2', num_publication='1234567', cle='8')
        self.assertTrue(isbn.is_valid_isbn())

    def test_invalid_isbn(self):
        isbn = ISBN(domaine='978', num_editeur='2', num_publication=1234567, cle='9')
        self.assertFalse(isbn.is_valid_isbn())
        