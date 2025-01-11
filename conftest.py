import pytest

from main import BooksCollector
# создаем экземпляр (объект) класса BooksCollector


pytest.fixture(scope='function') # фикстура, которая создаёт компанию
def new_book():
    collector = BooksCollector()
    # добавляем  книгу
    collector.add_new_book('Пикник на обочине')
    collector.add_new_book('Улитка на склоне')
    collector.set_book_genre('Пикник на обочине','Фантастика')
    collector.set_book_genre('Улитка на склоне','Фантастика')





    return collector.get_books_genre()