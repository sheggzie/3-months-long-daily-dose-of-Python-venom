# Create a script to calculate the area of a circle given its radius.

def area(radius):
    # Formular to get Area of a circle is "a = pi(3.14) * (power of r(radius))"
    a = 3.14 * pow(radius, 2)
    return int(a)

print(area(10))

