import os
import pytest
from books import BookCollection, Book

@pytest.fixture(autouse=True)
def use_temp_data_file(tmp_path, monkeypatch):
    temp_file = tmp_path / "data.json"
    temp_file.write_text("[]")
    monkeypatch.setattr("books.DATA_FILE", str(temp_file))


def test_add_book_valid():
    collection = BookCollection()
    # Valid year
    book = collection.add_book("Dune", "Frank Herbert", 1965)
    assert book.title == "Dune"
    assert book.author == "Frank Herbert"
    assert book.year == 1965
    assert not book.read
    assert collection.find_book_by_title("Dune") is not None
    # Invalid year: zero
    with pytest.raises(ValueError):
        collection.add_book("Zero Year Book", "Author", 0)
    # Invalid year: negative
    with pytest.raises(ValueError):
        collection.add_book("Negative Year Book", "Author", -2020)
    # Valid year: positive
    book2 = collection.add_book("Valid Year Book", "Author", 2020)
    assert book2.year == 2020


def test_add_book_empty_title():
    collection = BookCollection()
    with pytest.raises(ValueError):
        collection.add_book("", "Author", 2000)


def test_list_books():
    collection = BookCollection()
    collection.add_book("Dune", "Frank Herbert", 1965)
    books = collection.list_books()
    assert len(books) == 1
    assert books[0].title == "Dune"


def test_search_books_title():
    collection = BookCollection()
    collection.add_book("Dune", "Frank Herbert", 1965)
    results = collection.search_books("dune")
    assert len(results) == 1
    assert results[0].title == "Dune"


def test_search_books_author():
    collection = BookCollection()
    collection.add_book("Dune", "Frank Herbert", 1965)
    results = collection.search_books("frank")
    assert len(results) == 1
    assert results[0].author == "Frank Herbert"


def test_find_book_by_title_case_insensitive():
    collection = BookCollection()
    collection.add_book("Dune", "Frank Herbert", 1965)
    assert collection.find_book_by_title("dune") is not None
    assert collection.find_book_by_title("DUNE") is not None


def test_mark_as_read():
    collection = BookCollection()
    collection.add_book("Dune", "Frank Herbert", 1965)
    assert collection.mark_as_read("Dune")
    assert collection.find_book_by_title("Dune").read


def test_mark_as_read_not_found():
    collection = BookCollection()
    assert not collection.mark_as_read("Nonexistent")


def test_remove_book():
    collection = BookCollection()
    collection.add_book("Dune", "Frank Herbert", 1965)
    assert collection.remove_book("Dune")
    assert collection.find_book_by_title("Dune") is None


def test_remove_book_not_found():
    collection = BookCollection()
    assert not collection.remove_book("Nonexistent")


def test_find_by_author_case_insensitive():
    collection = BookCollection()
    collection.add_book("Dune", "Frank Herbert", 1965)
    collection.add_book("Book2", "frank herbert", 1970)
    results = collection.find_by_author("FRANK HERBERT")
    assert len(results) == 2


def test_list_by_year():
    collection = BookCollection()
    collection.add_book("Dune", "Frank Herbert", 1965)
    collection.add_book("Book2", "Author2", 1970)
    result = collection.list_by_year(1965, 1970)
    assert 1965 in result
    assert 1970 in result
    assert any(b.title == "Dune" for b in result[1965])
    assert any(b.title == "Book2" for b in result[1970])


def test_list_by_year_empty():
    collection = BookCollection()
    result = collection.list_by_year(2000, 2010)
    assert result == {}
