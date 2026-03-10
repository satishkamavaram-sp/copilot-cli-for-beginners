import sys
from books import BookCollection
from utils import print_books

# Removed show_books; consolidated display logic to print_books


# Global collection instance
collection = BookCollection()




def handle_list() -> None:
    books = collection.list_books()
    print_books(books)


def handle_add() -> None:
    print("\nAdd a New Book\n")

    title = input("Title: ").strip()
    author = input("Author: ").strip()
    year_str = input("Year: ").strip()

    # Validate year as positive integer, consistent with utils.py:get_book_details
    if not year_str:
        print("Year cannot be empty. Please enter a year, like 1999 or 2020.")
        return
    try:
        year = int(year_str)
        if year <= 0:
            print("Oops! The year must be a positive number, like 1999. Please try again.")
            return
    except ValueError:
        print("That doesn't look like a year. Please enter a number, like 1999.")
        return

    collection.add_book(title, author, year)
    print("\nBook added successfully.\n")


def handle_remove() -> None:
    print("\nRemove a Book\n")

    title = input("Enter the title of the book to remove: ").strip()
    collection.remove_book(title)

    print("\nBook removed if it existed.\n")


def handle_find() -> None:
    print("\nFind Books by Author\n")

    author = input("Author name: ").strip()
    books = collection.find_by_author(author)

    print_books(books)

def handle_search() -> None:
    print("\nSearch Books by Title\n")
    title = input("Title keyword: ").strip()
    books = collection.search_books(title)
    print_books(books)


def show_help() -> None:
    print("""
Book Collection Helper

Commands:
  list     - Show all books
  add      - Add a new book
  remove   - Remove a book by title
  find     - Find books by author
  help     - Show this help message
""")


def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    # Dictionary dispatch pattern for command handling
    commands = {
        "list": handle_list,
        "add": handle_add,
        "remove": handle_remove,
        "find": handle_find,
        "search": handle_search,
        "help": show_help
    }
    func = commands.get(command)
    if func:
        func()
    else:
        print("Unknown command.\n")
        show_help()


if __name__ == "__main__":
    main()
