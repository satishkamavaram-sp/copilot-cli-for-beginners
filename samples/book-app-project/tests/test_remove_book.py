import pytest
from books import BookCollection

def test_remove_existing_book():
    collection = BookCollection()
    collection.add_book("Dune", "Frank Herbert", 1965)
    msg = collection.remove_book("Dune")
    assert msg == 'Book "Dune" removed.'
    assert collection.find_book_by_title("Dune") is None

def test_remove_case_insensitive():
    collection = BookCollection()
    collection.add_book("Dune", "Frank Herbert", 1965)
    msg = collection.remove_book("dUnE")
    assert msg == 'Book "Dune" removed.'
    assert collection.find_book_by_title("Dune") is None

def test_remove_nonexistent_book():
    collection = BookCollection()
    msg = collection.remove_book("Nonexistent Book")
    assert msg == 'No book found with title "Nonexistent Book".'

def test_remove_from_empty_collection():
    collection = BookCollection()
    # Ensure collection is empty
    collection.books.clear()
    msg = collection.remove_book("Any Book")
    assert msg == 'No book found with title "Any Book".'
