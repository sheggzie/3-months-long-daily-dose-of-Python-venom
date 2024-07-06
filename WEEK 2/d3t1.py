# Create a script that reads a text file and prints its contents.

def display_text(filename="random.txt"):
    with open(filename, "r") as file:
        print(file.readlines())
display_text()