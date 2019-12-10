from unittest import TestCase
from phonebook import PhoneBook


class PhoneBookTest(TestCase):
    def test_create_phonebook(self):
        book = PhoneBook()

        self.assertEqual(0, len(book.entries))

    def test_add_entry(self):
        book = PhoneBook()

        book.add_entry('João', '(11) 1234 4321')

        self.assertEqual(1, len(book.entries))
