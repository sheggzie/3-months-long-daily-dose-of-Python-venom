# Write a program that creates multiple Person objects and displays their information.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"{self.name} is {self.age} years old.")

people = [
    Person("Sheggzie", 24),
    Person("Tola", 30),
    Person("Fola", 28),
    Person("Bola", 22)
]

for person in people:
    person.display_info()