# Tasks:
# COVID-19 Data Analysis and Visualization Project:
# Fetch COVID-19 data from a public API.
# Perform data analysis using pandas.
# Create visualizations using matplotlib and seaborn.

# Steps:
# Fetch COVID-19 data using the requests library.
# Load the data into a pandas DataFrame and perform basic data cleaning.
# Analyze the data to extract meaningful insights.
# Create visualizations to display the insights.

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

url = 'https://api.covidtracking.com/v1/us/daily.json'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    xlxs = df.to_excel('covid_report.xlsx', sheet_name='covid report')
    # print(data)
else:
    print(f"Error encountered! {response.status_code}")
