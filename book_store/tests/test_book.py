from lib.book import *

"""
Check if book properties exist
"""

def test_properties():
    book = Book(3, "Emma", "Jane Austen")
    assert book.id == 3
    assert book.title == "Emma"
    assert book.author_name == "Jane Austen"

"""
Check Book can be nicely formatted
"""

def test_books_nicely_formatted():
    book = Book(3, "Emma", "Jane Austen")
    assert str(book) == "Book(3, Emma, Jane Austen)"

"""
Check if we compare two book objects
We have them as equal
"""

def test_books_are_equal():
    book1 = Book(3, "Emma", "Jane Austen")
    book2 = Book(3, "Emma", "Jane Austen")
    assert book1 == book2