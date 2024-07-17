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
        title = input("Enter the book Title: ").strip()
        author = input("Enter the book Author: ").strip()
        year = input("Enter the Year the book was published: ").strip()

        if not year.isdigit():
            print("Error! Year must be a number.")
            return

        with open(filename, "a", newline="") as file:
            lines = csv.writer(file)
            lines.writerow([title, author, year])
        print(f"Book '{title}' by {author} added succesfully.")                
        
    def remove_book():
        prompt = input("Enter the title of the book to remove: ").strip().lower()
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
        prompt = input("Enter the title or author of the book to check: ").strip().lower()
        found = False

        with open(filename, "r") as file:
            lines = csv.reader(file)

            for row in lines:
                if prompt in row[0].lower() or prompt in row[1].lower():
                    print("Book found, check below for details:") 
                    print(f"Title: {row[0]}")
                    print(f"Author: {row[1]}")
                    print(f"Year: {row[2]}", "\n")
                    found = True
            
            if not found:
                print(f"No book with title and author '{prompt}' found!")

    def list_books():
        with open(filename, "r") as file:
            lines = csv.reader(file)
            books = list(lines)

        if not books:
            print("No book found!")
            return
        
        print("="*65)
        print(f"{'TITLE':<30}{'AUTHOR':<30}{'YEAR':<5}" + "\n")
        for title, author, year in books:
            print(f"{title:<30}{author:<30}{year:<5}")
        print("="*65 + "\n")
        
        


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
                print("Exiting Book Manager...")
                break
            case _:
                print("Error! Enter a valid prompt!")
booker()