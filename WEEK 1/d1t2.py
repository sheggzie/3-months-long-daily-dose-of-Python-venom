# Write a program that converts Celsius to Fahrenheit.

# Formular for Fahrenheit is F = C * (9/5) + 32

def convert_temp(celcius):
    f = celcius * (9/5) + 32
    return f

print(int(convert_temp(100)))