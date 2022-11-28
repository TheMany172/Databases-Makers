from lib.book import *

class BookRepository:
    def __init__(self,connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM books')
        book_list = []
        for row in rows:
            item = f"{row['id']} - {row['title']} - {row['author_name']}"
            book_list.append(item)
        return book_list