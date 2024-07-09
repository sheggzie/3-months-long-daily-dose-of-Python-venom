# Create a script that reads a file of student names and scores, stores them in a dictionary, and performs various operations.
import csv

students = {}
filename = "student records.txt"

def records(filename):
    global students
    with open(filename, "r") as file:
        lines = csv.reader(file)
        
        for name, scores in lines:
            students[name] = int(scores)
    return students

def add_record(name, score):
    global students
    students[name] = int(score)
    print(f"Student name: {name} with score: {score} added to students")
    print(students)   

def remove_student(students, name):
    if name in students:
        del students[name]
        print(f"Student with name: {name} removed.")
    else:
        print("Students record not found!")

def get_top_scorer():
    top_scorer = max(students.values())
    for key, value in students.items():
        if value == top_scorer:
            print(f"The student with the highest score is {key} with score {top_scorer}")
            return key       
    

def save_records(filename, students):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for name, score in students.items():
            writer.writerow([name, score])



def main():
    students = records(filename)
    while True:
        print("Enter 1 to add record.")
        print("Enter 2 to remove a student record.")
        print("Enter 3 to see the top scoring student.")
        print("Enter x to exit.")
        prompt = input("What do you want to do? ")
        if prompt == "1":
            name = input("Enter student name: ")
            score = input("Enter student score: ")
            add_record(name, score)
        elif prompt == "2":
            ask = input("Enter name of Student to remove: ")
            remove_student(students, ask)
        elif prompt == "3":
            get_top_scorer()
        elif prompt == "x":
            save_records(filename, students)
            break
main()