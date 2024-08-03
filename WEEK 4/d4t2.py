# Generate a bar chart and customize its appearance.

import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 4]

plt.bar(categories, values, color=["red", "green", "blue", "yellow"]) # create and customize bar
plt.title("Bar chart", fontsize=20, fontweight='bold') # title and customize bar
plt.xlabel("Categories", fontsize=15) # name and customize x axis
plt.ylabel("Values", fontsize=15) # name and customize y axis
plt.xticks(fontsize=12) # customize ticks fontsize
plt.yticks(fontsize=12) # customize ticks fontsize

# add gridlines
plt.grid(linestyle='dashed')

plt.show() # show chart