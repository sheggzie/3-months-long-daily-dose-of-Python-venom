# Create a Student class that inherits from the Person class and adds additional attributes and methods.

# create class Person and initialize name and age parameter
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"{self.name} is {self.age} years old.") # print message with the given input for name and age

# create a new class that Inherits functionality from Person class
class Students(Person):
    def __init__(self, name, age, id, level):
        super().__init__(name, age)     # Inherit name and age functionality from Person class   
        self.id = id
        self.level = level

    # display messages in the print function with respective parameter inputs
    def display_info(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")
        print(f"My ID num is {self.id}")
        print(f"I am currently in level {self.level}")

student1 = Students("Tola", 15, 15151515, 200) # assign student class and it's specified parameters to student1
student1.display_info() # call the display_info() function 