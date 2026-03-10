import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import books
from books import BookCollection


@pytest.fixture(autouse=True)
def use_temp_data_file(tmp_path, monkeypatch):
    """Use a temporary data file for each test."""
    temp_file = tmp_path / "data.json"
    temp_file.write_text("[]")
    monkeypatch.setattr(books, "DATA_FILE", str(temp_file))


def test_add_book():
    # Existing valid add_book test
    collection = BookCollection()
    initial_count = len(collection.books)
    collection.add_book("1984", "George Orwell", 1949)
    assert len(collection.books) == initial_count + 1
    book = collection.find_book_by_title("1984")
    assert book is not None
    assert book.author == "George Orwell"
    assert book.year == 1949
    assert book.read is False

import pytest

def test_add_book_invalid_year():
    collection = BookCollection()
    with pytest.raises(ValueError):
        collection.add_book("Bad Year", "Author", 0)
    with pytest.raises(ValueError):
        collection.add_book("Bad Year", "Author", -1990)
    with pytest.raises(ValueError):
        collection.add_book("Bad Year", "Author", "not a year")

    collection = BookCollection()
    initial_count = len(collection.books)
    # Valid year
    collection.add_book("1984", "George Orwell", 1949)
    assert len(collection.books) == initial_count + 1
    book = collection.find_book_by_title("1984")
    assert book is not None
    assert book.author == "George Orwell"
    assert book.year == 1949
    assert book.read is False
    # Invalid year: zero
    with pytest.raises(ValueError):
        collection.add_book("Zero Year Book", "Author", 0)
    # Invalid year: negative
    with pytest.raises(ValueError):
        collection.add_book("Negative Year Book", "Author", -2020)
    # Valid year: positive
    book2 = collection.add_book("Valid Year Book", "Author", 2020)
    assert book2.year == 2020

def test_mark_book_as_read():
    collection = BookCollection()
    collection.add_book("Dune", "Frank Herbert", 1965)
    result = collection.mark_as_read("Dune")
    assert result is True
    book = collection.find_book_by_title("Dune")
    assert book.read is True

def test_mark_book_as_read_invalid():
    collection = BookCollection()
    result = collection.mark_as_read("Nonexistent Book")
    assert result is False

def test_remove_book():
    collection = BookCollection()
    collection.add_book("The Hobbit", "J.R.R. Tolkien", 1937)
    result = collection.remove_book("The Hobbit")
    assert result is True
    book = collection.find_book_by_title("The Hobbit")
    assert book is None

def test_remove_book_invalid():
    collection = BookCollection()
    result = collection.remove_book("Nonexistent Book")
    assert result is False


def test_search_books_partial_title():
    collection = BookCollection()
    collection.add_book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997)
    collection.add_book("Harry Potter and the Chamber of Secrets", "J.K. Rowling", 1998)
    collection.add_book("The Hobbit", "J.R.R. Tolkien", 1937)
    results = [b.title for b in collection.list_books() if "Harry" in b.title]
    assert len(results) == 2
    assert "Harry Potter and the Sorcerer's Stone" in results
    assert "Harry Potter and the Chamber of Secrets" in results


def test_search_books_partial_author():
    collection = BookCollection()
    collection.add_book("1984", "George Orwell", 1949)
    collection.add_book("Animal Farm", "George Orwell", 1945)
    collection.add_book("Brave New World", "Aldous Huxley", 1932)
    results = [b.title for b in collection.list_books() if "Orwell" in b.author]
    assert len(results) == 2
    assert "1984" in results
    assert "Animal Farm" in results


def test_search_books_no_matches():
    collection = BookCollection()
    collection.add_book("Dune", "Frank Herbert", 1965)
    results = [b.title for b in collection.list_books() if "Potter" in b.title]
    assert results == []


def test_search_books_multiple_matches():
    collection = BookCollection()
    collection.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    collection.add_book("Great Expectations", "Charles Dickens", 1861)
    collection.add_book("The Greatest Show on Earth", "Richard Dawkins", 2009)
    results = [b.title for b in collection.list_books() if "Great" in b.title]
    assert len(results) == 3
    assert "The Great Gatsby" in results
    assert "Great Expectations" in results
    assert "The Greatest Show on Earth" in results


def test_list_by_year_empty_collection():
    collection = BookCollection()
    results = collection.list_by_year(2000, 2020)
    assert results == []


def test_list_by_year_no_books_in_range():
    collection = BookCollection()
    collection.add_book("Book1", "Author1", 1990)
    collection.add_book("Book2", "Author2", 1995)
    results = collection.list_by_year(2000, 2020)
    assert results == []


def test_list_by_year_multiple_books_per_year():
    collection = BookCollection()
    collection.add_book("BookA", "AuthorA", 2001)
    collection.add_book("BookB", "AuthorB", 2001)
    collection.add_book("BookC", "AuthorC", 2002)
    collection.add_book("BookD", "AuthorD", 2002)
    results = collection.list_by_year(2001, 2002)
    years = [b.year for b in results]
    assert years.count(2001) == 2
    assert years.count(2002) == 2
    assert len(results) == 4


def test_list_by_year_start_greater_than_end():
    collection = BookCollection()
    collection.add_book("BookX", "AuthorX", 2010)
    results = collection.list_by_year(2020, 2010)
    assert results == []
