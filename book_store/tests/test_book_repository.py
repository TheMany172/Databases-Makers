from lib.book_repository import *
from lib.book import *

"""
When we call BookRepository.all()
We get a list of all Book objects reflecting the seed data in book_store.sql
"""

def test_all_books(db_connection):
    db_connection.seed('seeds/book_store.sql')
    repository = BookRepository(db_connection)

    books = repository.all()

    assert books == [
        "1 - Nineteen Eighty-Four - George Orwell",
        "2 - Mrs Dalloway - Virginia Woolf",
        "3 - Emma - Jane Austen",
        "4 - Dracula - Bram Stoker",
        "5 - The Age of Innocence - Edith Wharton"
    ]