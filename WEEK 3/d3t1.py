# Create a Person class with attributes for name and age, and methods to display the person's information.

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"{self.name} is {self.age} years old.")


newPerson = Person("Sheggzie", 24)

newPerson.display_info()

