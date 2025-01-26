BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

from pydantic import BaseModel

# TODO написать класс Book

class Book(BaseModel):
    id: int
    name: str
    pages: int


# TODO написать класс Library

from typing import List
from typing import Optional



class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books
        self.get_next_book_id()

    next_book_id = 1   #идентификатор, когда книг в библиотеке нет
   
    def get_next_book_id(self, books=None):
        if books is None:
            return next_book_id



if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
