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
    # load data into Pandas dataframe
    data = response.json()
    df = pd.DataFrame(data)
    
    # perform basic data operations
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d') # convert date int to actual datetime
    df.set_index('date', inplace=True)    # set date as index
    df.sort_index(inplace=True) 
    print(df.head())
    # xlxs = df.to_excel('covid_report.xlsx', sheet_name='covid report')

    # analyze and visualize data with MatPlotLib and
    
    # Daily Increase in Positive Cases
    plt.figure(figsize=(14, 7))
    sbn.lineplot(data=df, x='date', y='positiveIncrease')
    plt.title('Daily Increase in Positive COVID-19 Cases in the US')
    plt.xlabel('Date')
    plt.ylabel('Positive Increase')
    plt.xticks(rotation=45)
    plt.show()    

    # Daily Increase in Deaths
    plt.figure(figsize=(14, 7))
    sbn.lineplot(data=df, x='date', y='deathIncrease')
    plt.title('Daily Increase in COVID-19 Deaths in the US')
    plt.xlabel('Date')
    plt.ylabel('Death Increase')
    plt.xticks(rotation=45)
    plt.show()
else:
    print(f"Error encountered! {response.status_code}")