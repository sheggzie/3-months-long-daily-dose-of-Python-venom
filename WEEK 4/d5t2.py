# Generate a box plot to display distributions.

import seaborn as sbn
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance', 'HR', 'IT'],
    'Salary': [60000, 75000, 50000, 85000, 90000, 70000, 55000, 65000],
    'Years_Experience': [2, 5, 3, 7, 8, 4, 2, 3],
    'Age': [25, 30, 22, 35, 40, 28, 24, 26]
}

df = pd.DataFrame(data)

# Create a box plot
plt.figure(figsize=(10, 8))
sbn.boxplot(x='Department', y='Salary', data=df)
plt.title("Salary Distribution by department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()