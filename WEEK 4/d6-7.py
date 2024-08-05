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

data = response.json()

print(data)