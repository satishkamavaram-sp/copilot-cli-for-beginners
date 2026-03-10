import json
from dataclasses import dataclass, asdict
from typing import List, Optional

DATA_FILE = "data.json"


@dataclass
class Book:
    title: str
    author: str
    year: int
    read: bool = False


class BookCollection:
    def __init__(self):
        """
        Initialize a new BookCollection instance and load books from the data file.
        """
        self.books: List[Book] = []
        self.load_books()

    def load_books(self):
        """
        Load books from the JSON file if it exists.
        Parameters:
            None
        Returns:
            None
        """
        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.books = [Book(**b) for b in data]
        except FileNotFoundError:
            self.books = []
        except json.JSONDecodeError:
            print("Warning: data.json is corrupted. Starting with empty collection.")
            self.books = []

    def save_books(self):
        """
        Save the current book collection to JSON.
        Parameters:
            None
        Returns:
            None
        """
        with open(DATA_FILE, "w") as f:
            json.dump([asdict(b) for b in self.books], f, indent=2)

    def add_book(self, title: str, author: str, year: int) -> Book:
        """
        Add a new book to the collection.
        Parameters:
            title (str): The title of the book. Must not be empty.
            author (str): The author of the book.
            year (int): The publication year of the book.
        Returns:
            Book: The Book object that was added.
        Raises:
            ValueError: If the title is empty.
        """
        if not title.strip():
            raise ValueError("Book title cannot be empty.")
        if not isinstance(year, int) or year <= 0:
            raise ValueError("The year must be a positive number, like 1999. Please enter a valid year.")
        book = Book(title=title, author=author, year=year)
        self.books.append(book)
        self.save_books()
        return book

    def list_books(self) -> List[Book]:
        """
        Get the list of all books in the collection.
        Parameters:
            None
        Returns:
            List[Book]: List of all Book objects in the collection.
        """
        return self.books

    def search_books(self, query: str) -> List[Book]:
        """
        Search for books where the query matches a partial, case-insensitive substring in the title or author.
        Parameters:
            query (str): The search string to match against book titles and authors.
        Returns:
            List[Book]: List of Book objects matching the query.
        """
        query_lower = query.lower()
        return [
            book
            for book in self.books
            if query_lower in book.title.lower() or query_lower in book.author.lower()
        ]

    def find_book_by_title(self, title: str) -> Optional[Book]:
        """
        Find a book in the collection by its title (case-insensitive).
        
        Parameters:
            title (str): The title of the book to search for.
        
        Returns:
            Optional[Book]: The Book object if found, else None.
        
        Example:
            >>> collection.find_book_by_title('Dune')
            Book(title='Dune', author='Frank Herbert', year=1965, read=False)
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def mark_as_read(self, title: str) -> bool:
        """
        Mark a book as read by its title.
        
        Parameters:
            title (str): The title of the book to mark as read.
        
        Returns:
            bool: True if the book was found and marked as read, False otherwise.
        
        Example:
            >>> collection.mark_as_read('Dune')
            True
        """
        book = self.find_book_by_title(title)
        if book:
            book.read = True
            self.save_books()
            return True
        return False

    def remove_book(self, title: str) -> str:
        """
        Remove a book from the collection by its title (case-insensitive, trims whitespace).
        
        Parameters:
            title (str): The title of the book to remove.
        
        Returns:
            str: Feedback message about the removal result.
        
        Example:
            >>> collection.remove_book('Dune')
            'Book "Dune" removed.'
        """
        title_clean = title.strip().lower()
        for book in self.books:
            if book.title.strip().lower() == title_clean:
                self.books.remove(book)
                self.save_books()
                return f'Book "{book.title}" removed.'
        return f'No book found with title "{title.strip()}".'

    def find_by_author(self, author: str) -> List[Book]:
        """
        Find all books in the collection by a given author (case-insensitive).
        
        Parameters:
            author (str): The author name to search for.
        
        Returns:
            List[Book]: List of Book objects by the specified author.
        
        Example:
            >>> collection.find_by_author('Frank Herbert')
            [Book(title='Dune', author='Frank Herbert', year=1965, read=False)]
        """
        return [b for b in self.books if b.author.lower() == author.lower()]

    def list_by_year(self, start: int, end: int) -> dict:
        """
        List books published in each year within a given range.
        
        Parameters:
            start (int): The start year (inclusive).
            end (int): The end year (inclusive).
        
        Returns:
            dict: A dictionary mapping each year to a list of Book objects published that year.
        
        Example:
            >>> collection.list_by_year(1960, 1970)
            {1965: [Book(title='Dune', author='Frank Herbert', year=1965, read=False)]}
        """
        result = {}
        for year in range(start, end + 1):
            books_in_year = [b for b in self.books if b.year == year]
            if books_in_year:
                result[year] = books_in_year
        return result

