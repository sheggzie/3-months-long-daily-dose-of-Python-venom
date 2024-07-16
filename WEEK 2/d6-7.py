# Book Catalog Project:
# Create a command-line interface (CLI) book catalog.
# Features to implement:
# Add a book (title, author, year)
# Remove a book
# Search for a book by title or author
# List all books
# Store books in a file so they persist between program runs.

import csv

filename = "books.csv"

with open(filename, "w") as file:
    line = csv.writer(file)
    line.writerow(["title", "author", "year"])


def booker():
    def add_book():
        title = input("Enter the book Title: ")
        author = input("Enter the book Author: ")
        year = input("Enter the Year the book was published: ")
        with open(filename, "a", newline="") as file:
            lines = csv.writer(file)
            lines.writerow([title, author, year])                
        
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