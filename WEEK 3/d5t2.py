# Write a program that manages courses and students, allowing the addition of students 
# to courses and displaying course information.

class Manager:
    def __init__(self):
        self.student_name = []
        self.student_id = []
        self.course = {
            "Biology": 112,
            "Mathematics": 113,
            "English": 222,
            "Physics": 333,
            "Chemistry": 555
                       }        

    def add_student(self):
        name = input("Enter student's name: ")
        id = input("Enter student's ID number: ")
        coursename = input("Enter coursename: ")
        
        self.student_name.append(name)
        self.student_id.append(id)
        print(f"{name} with Student ID: {id} has been registered for Course: {coursename} with Coursecode: {self.course[coursename]}")

manage = Manager()
while True:
    prompt = input("Enter a prompt: ")
    match prompt:
        case "add student":
            manage.add_student()
        case "list students":
            pass
        case "list courses":
            pass
        case "end" | "close" | "quit":
            break
