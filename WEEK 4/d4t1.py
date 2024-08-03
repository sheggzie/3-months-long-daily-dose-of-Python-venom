# Create a line plot of a dataset.

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# create plot
plt.plot(x, y)

plt.title("Line plot") # title plot
plt.xlabel("x axis") # name x axis
plt.ylabel("y axis") # name y axis

plt.show()