def print_menu() -> None:
    print("\n📚 Book Collection App")
    print("1. Add a book")
    print("2. List books")
    print("3. Mark book as read")
    print("4. Remove a book")
    print("5. Exit")


def get_user_choice() -> str:
    while True:
        choice = input("Choose an option (1-5): ").strip()

        if not choice:
            print("Choice cannot be empty. Please enter a number.")
            continue
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        if choice not in {"1", "2", "3", "4", "5"}:
            print("Choice must be between 1 and 5.")
            continue

        return choice


from typing import Tuple

def get_book_details() -> Tuple[str, str, int]:
    """
    Prompt the user to enter book details and validate input.

    Parameters:
        None

    Returns:
        tuple[str, str, int]:
            - title (str): The title of the book (non-empty).
            - author (str): The author of the book (non-empty).
            - year (int): The publication year (positive integer).
    """
    while True:
        title = input("Enter book title: ").strip()
        if not title:
            print("Title cannot be empty. Please enter a title.")
            continue
        break

    author = input("Enter author: ").strip()
    while not author:
        print("Author cannot be empty. Please enter an author.")
        author = input("Enter author: ").strip()

    while True:
        year_input = input("Enter publication year: ").strip()
        if not year_input:
            print("Year cannot be empty. Please enter a year, like 1999 or 2020.")
            continue
        try:
            year = int(year_input)
            if year <= 0:
                print("Oops! The year must be a positive number, like 1999. Please try again.")
                continue
            break
        except ValueError:
            print("That doesn't look like a year. Please enter a number, like 1999.")
    return title, author, year


from typing import List, Any

def format_books(books: List[Any]) -> List[str]:
    if not books:
        return ["No books in your collection."]

    lines = ["\nYour Books:"]
    for index, book in enumerate(books, start=1):
        try:
            status = "✅ Read" if getattr(book, 'read', False) else "📖 Unread"
            title = getattr(book, 'title', 'Unknown Title')
            author = getattr(book, 'author', 'Unknown Author')
            year = getattr(book, 'year', 'Unknown Year')
            lines.append(f"{index}. {title} by {author} ({year}) - {status}")
        except Exception as e:
            lines.append(f"{index}. Error displaying book: {e}")
    return lines

def print_books(books: List[Any]) -> None:
    for line in format_books(books):
        print(line)

