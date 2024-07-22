# Create a Course class and a Student class, where a Course can have multiple Student objects.

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

class Course:
    def __init__(self, coursename, coursecode):
        self.coursename = coursename
        self.coursecode = coursecode
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} with Student ID: {student.student_id} has registered for Course: {self.coursename} with Coursecode: {self.coursecode}")


# Creating Student objects
student1 = Student("Quadri", 8482928482)
student2 = Student("Tola", 15151515)

# Creating a Course object
course1 = Course("Biology", 838)
course2 = Course("Math", 387)

# Registering students to the course
course1.add_student(student1)
course1.add_student(student2)
course2.add_student(student1)
course2.add_student(student2)