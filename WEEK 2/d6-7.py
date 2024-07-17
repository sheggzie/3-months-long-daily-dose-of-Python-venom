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

def booker():    
    print("WELCOME TO THE BOOK MANAGER!")
    print("Enter 'i' to get info on prompts to run the program." + '\n')

    def show_info():
        print("1. 'add book' to add book.")
        print("2. 'remove book' to remove book.")
        print("3. 'list books' to show available books.")
        print("4. 'query book' to search a book.")
        print("5. 'exit' | 'close' | 'quit' | 'end' when done to exit!" + '\n')

    def add_book():
        title = input("Enter the book Title: ")
        author = input("Enter the book Author: ")
        year = input("Enter the Year the book was published: ")

        with open(filename, "a", newline="") as file:
            lines = csv.writer(file)
            lines.writerow([title, author, year])                
        
    def remove_book():
        prompt = input("Enter the title of the book to remove: ")
        found = False

        with open(filename, "r", newline="") as file:
            lines = csv.reader(file)
            rows = list(lines)

        for i, row in enumerate(rows):
            if row[0] == prompt:
                found = True
                del rows[i]
                break

        if not found:
            print(f"Book titled {prompt} is not found!")
        else:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print(f"Book titled '{prompt}' has been removed successfully.")

    def search_book():
        prompt = input("Enter the title of the book to check: ")
        with open(filename, "r") as file:
            lines = csv.reader(file)
            rows = list(lines)

            for i, row in enumerate(rows):
                if row[0] == prompt:
                    print("Check the details of your search below: ") 
                    print(f"Title: {row[0]}")
                    print(f"Author: {row[1]}")
                    print(f"Year: {row[2]}", "\n")  

    def list_books():
        with open(filename, "r") as file:
            lines = csv.reader(file)
            for title, author, year in lines:
                print("title: ", title)
                print("author: ", author)
                print("year: ", year + "\n")


    while True:
        prompt = input("Enter a prompt: ").strip().lower()
        match prompt:
            case 'i':
                show_info()
            case "add book":
                add_book()
            case "remove book":
                remove_book()
            case "list books":
                list_books()
            case "query book":
                search_book()
            case "exit" | "close" | "quit" | "end":
                break
            case _:
                print("Error! Enter a valid prompt!")
booker()