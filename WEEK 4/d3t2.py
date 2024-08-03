# Analyze a dataset by grouping and aggregating data.

import pandas as pd

data = {
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance', 'HR', 'IT'],
    'Employee': ['John', 'Jane', 'Doe', 'Mary', 'Peter', 'Paul', 'Mark', 'Lucy'],
    'Salary': [60000, 75000, 50000, 85000, 90000, 70000, 55000, 65000],
    'Years_Experience': [2, 5, 3, 7, 8, 4, 2, 3]
}

df = pd.DataFrame(data)

grouped = df.groupby('Department') # group by department

# get average salary by department
avg_salary = grouped['Salary'].mean().round(2)

# get average years of experience
avg_yoe = grouped['Years_Experience'].mean().round(2)

# get total salary by department
total_salary = grouped['Salary'].sum()

# aggregate data
agg_data = grouped.agg({
    'Salary':['mean', 'max', 'min', 'sum'],
    'Years_Experience':['mean', 'min', 'max']
}).round(2)

print(agg_data)