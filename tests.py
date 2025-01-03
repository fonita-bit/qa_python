from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

        # --1--  --тест не добавления новой книги  (в названии больше 40 символов)--
        def test_add_new_book_add_book_name_len_more_than40(self):
            # создаем экземпляр (объект) класса BooksCollector
            collector = BooksCollector()

            # добавляем книгу в названии, которой больше 40 символов 54 без пробелов 47
            collector.add_new_book('Клуб любителей книг и пирогов из картофельных очистков')
            # проверяем, что книга не добавилась
            # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 0
            assert len(collector.get_books_genre()) == 0

            # --2-- --устанавливаем книге жанр, который есть в списке--

        def test_set_book_genre_add_book_with_genre(self, new_book):
            assert len(new_book) == 2

            # --3-- --тест получает жанр книги по её имени--

        def test_get_book_genre_add_one_book(self, new_book):
            collector = BooksCollector()
            collector.books_genre = new_book
            assert collector.get_book_genre('Пикник на обочине') == 'Фантастика'

            # --4-- --тест проверяет список из двух книг с жанром фантастика--

        def test_get_books_with_specific_genre_add_two_books_fantasy_genre(self, new_book):
            collector = BooksCollector()
            collector.books_genre = new_book
            assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

            # --5-- --тест на получение словаря books_genre--

        def test_get_books_genre__add_books(self, new_book):
            collector = BooksCollector()
            collector.books_genre = new_book
            assert collector.get_books_genre() == new_book

            # --6-- --тест не возвращает книги, неподходящие детям--

        def test_get_books_for_children_add_book_not_for_children_result_null(self):
            collector = BooksCollector()
            collector.add_new_book('Молчание ягнят')
            collector.set_book_genre('Молчание ягнят', 'Ужасы')
            assert len(collector.get_books_for_children()) == 0

            # --7-- --тест на добавление книги в Избранное--

        def test_add_book_in_favorites_add_one_book(self, new_book):
            collector = BooksCollector()
            collector.books_genre = new_book
            collector.add_book_in_favorites('Пикник на обочине')
            assert len(collector.get_list_of_favorites_books()) == 1

            # --8-- --тест на удаление книги из Избранного--

        def test_delete_book_from_favorites_add_one_book_del_one_book_result_null(self, new_book):
            collector = BooksCollector()
            collector.books_genre = new_book
            collector.add_book_in_favorites('Пикник на обочине')
            collector.delete_book_from_favorites('Пикник на обочине')
            assert len(collector.get_list_of_favorites_books()) == 0

            # --9-- --тест на получение списка Избранных книг--

        def test_get_list_of_favorites_books_add_two_books(self, new_book):
            collector = BooksCollector()
            collector.books_genre = new_book
            collector.add_book_in_favorites('Пикник на обочине')
            collector.add_book_in_favorites('Улитка на склоне')
            assert len(collector.get_list_of_favorites_books()) == 2

