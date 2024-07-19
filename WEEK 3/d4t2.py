# Write a program that demonstrates method overriding and polymorphism.

# METHOD OVERRIDING

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

fast.run()
faster.run() # Overrides the inherited run output and prints "I can run faster" 
