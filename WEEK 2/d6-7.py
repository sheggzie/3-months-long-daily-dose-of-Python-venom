# Book Catalog Project:
# Create a command-line interface (CLI) book catalog.
# Features to implement:
# Add a book (title, author, year)
# Remove a book
# Search for a book by title or author
# List all books
# Store books in a file so they persist between program runs.

def booker():
    def add_book():
        pass

    def remove_book():
        pass

    def list_books():
        pass


    while True:
        prompt = input("Enter a prompt: ")
        match prompt:
            case "add book":
                add_book()
            case "remove book":
                remove_book()
            case "list books":
                list_books()
            case "exit" | "close" | "quit":
                break
booker()