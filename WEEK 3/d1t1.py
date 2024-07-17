# Create a script that handles division by zero errors.

def divide(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        print("Division by 0 is not possible, enter a number greater or equal to 1")
print(divide(5,2.5))