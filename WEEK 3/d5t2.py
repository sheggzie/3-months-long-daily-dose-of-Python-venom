# Write a program that manages courses and students, allowing the addition of students 
# to courses and displaying course information.

class Manager:
    def __init__(self):
        self.student_name = []
        self.student_id = []
        self.course_entry = {
            "Biology":[],
            "Mathematics": [],
            "English": [],
            "Physics": [],
            "Chemistry": []
        }
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
        self.course_entry[coursename].append(name)
        print(f"{name} with Student ID: {id} has been registered for Course: {coursename} with Coursecode: {self.course[coursename]}")

    def display_courses(self):
        print("="*40)
        for course, code in self.course.items():
            print(f"{course:<20}{code:>20}")
        print("="*40)

    def course_info(self):
        print("="*30)
        for course, students in self.course_entry.items():
            print(f"{course:<15}{len(students):>15}")
        print("="*30)
            
manage = Manager()
while True:
    prompt = input("Enter a prompt: ")
    match prompt:
        case "add student":
            manage.add_student()
        case "list courses":
            manage.display_courses()
        case "registered course":
            manage.course_info()
        case "end" | "close" | "quit":
            break
        case _:
            print("Error! Enter a valid prompt!")
