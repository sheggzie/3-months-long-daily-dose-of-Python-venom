# Create a script that reads a file of student names and scores, stores them in a dictionary, and performs various operations.

def students(filename="records.txt"):
    with open(filename, "r") as file:
        file.readlines()