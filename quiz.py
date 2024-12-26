
class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}")

    def lend_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN and book not in self.borrowed_books:
                self.borrowed_books.append(book)
                print(f"Book '{book.title}' has been lent out.")
                return
        print(f"Book with ISBN {ISBN} is not available.")


class Report:
    def generate(self, library):
        pass


class BookReport(Report):
    def generate(self, library):
        print("\nLibrary Book Report:")
        for book in library.books:
            if book in library.borrowed_books:
                status = "Borrowed"
            else:
                status = "Available"

            print(f"- {book.title} by {book.author} (ISBN: {book.ISBN}, Status: {status})")



class NotificationService:
    def send_notification(self, message):
        print(f"Notification: {message}")



class LibraryService:
    def __init__(self, library, report):
        self.library = library
        self.report = report

    def generate_report(self):
        self.report.generate(self.library)




library = Library()
book1 = Book("2016", "It Ends With Us", "9781501110368")
book2 = Book("Believe in Yourself", "Dr Joseph Murphy", "9788183225090")


library.add_book(book1)
library.add_book(book2)


library.lend_book("987654321")


report = BookReport()
service = LibraryService(library, report)
service.generate_report()


notification_service = NotificationService()
notification_service.send_notification("Your book will be available tomorrow")

