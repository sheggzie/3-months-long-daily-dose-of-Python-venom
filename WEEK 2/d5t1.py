# Create a script that reads a file of student names and scores, stores them in a dictionary, and performs various operations.
import csv

students = {}
filename = "records.csv"

def records(filename):
    with open(filename, "r") as file:
        lines = csv.reader(file)
        
        for name, scores in lines:
            students[name] = int(scores)

def add_record(name, score):
    students[name] = int(score)
    print(f"Student name: {name} with score: {score} added to students")
    print(students)   

def save_records(filename, students):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for name, score in students.items():
            writer.writerow([name, score])


while True:
    print("Enter 1 to add record")
    print("Enter x to exit")
    prompt = input("What do you want to do? ")
    if prompt == "1":
        name = input("Enter student name: ")
        score = input("Enter student score: ")
        add_record(name, score)
    elif prompt == "x":
        save_records(filename, students)
        break