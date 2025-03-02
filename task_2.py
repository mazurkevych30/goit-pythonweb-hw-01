from abc import ABC, abstractmethod
from logger import logger


class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title: str = title
        self.author: str = author
        self.year: str = year


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, title: str, author: str, year: str) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books: list[dict[str, str]] = []

    def add_book(self, title: str, author: str, year: str) -> None:
        book: dict[str, str] = {"title": title, "author": author, "year": year}
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                break

    def show_books(self) -> None:
        for book in self.books:
            logger.info(
                "Title: %s, Author: %s, Year: %s",
                book["title"],
                book["author"],
                book["year"],
            )


class LibraryManager:
    def __init__(self, library_abstract: LibraryInterface):
        self.library_abstract: LibraryInterface = library_abstract

    def add_book(self, title: str, author: str, year: str) -> None:
        self.library_abstract.add_book(title, author, year)

    def remove_book(self, title: str) -> None:
        self.library_abstract.remove_book(title)

    def show_books(self) -> None:
        self.library_abstract.show_books()


def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
