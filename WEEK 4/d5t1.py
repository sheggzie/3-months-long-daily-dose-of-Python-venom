# Create a heatmap to visualize correlations in a dataset.

import seaborn as sbn
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance', 'HR', 'IT'],
    'Salary': [60000, 75000, 50000, 85000, 90000, 70000, 55000, 65000],
    'Years_Experience': [2, 5, 3, 7, 8, 4, 2, 3],
    'Age': [25, 30, 22, 35, 40, 28, 24, 26]
}

df = pd.DataFrame(data)

# select only numeric columns
num_data = df.select_dtypes(include='number')

# calculate the correlation matrix
correlation_matrix = num_data.corr()

# plot the heatmap
plt.figure(figsize=(10, 8))
sbn.heatmap(correlation_matrix, annot=True)
plt.title("Correlation Heatmap")
plt.show()