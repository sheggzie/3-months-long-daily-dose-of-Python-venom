# Write a script that uses the math module to perform advanced calculations.

import math

def get_power(base, power):
    # Get the base and power values as parameters and output the result
    result = math.pow(base, power)
    # Print the output without decimal using the math.ceil() function
    print(f"The power of {base} raised to the power of {power} is {math.ceil(result)}")

get_power(4, 2)