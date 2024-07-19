# Write a program that demonstrates method overriding and polymorphism.

# 1. METHOD OVERRIDING

# declare class Horse
class Horse:
    def run(self):
        print("I can run.")

# declare class Cheetah which inherits from Horse
class Cheetah(Horse):
    def run(self):
        print("I can run faster!")

fast = Horse()
faster = Cheetah()

# fast.run()
# faster.run() # Overrides the inherited run output and prints "I can run faster" 




# 2. POLYMORPHISM

# declare class Horse
class Horse:
    def run(self):
        print("I can run.")

# declare class Cheetah which inherits from Horse
class Cheetah(Horse):
    def run(self):
        print("I can run fasterrrrrrrr!")

# Polymorphing function that outputs based on class passed as parameter
def runner(animal):
    animal.run()

horse = Horse()
cheetah = Cheetah()

runner(horse)
runner(cheetah)