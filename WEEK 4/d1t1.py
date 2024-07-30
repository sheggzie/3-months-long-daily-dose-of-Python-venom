# Use the requests library to fetch data from a URL.

import requests

# get bitcoin price data from coindesk api
def fetcher():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
        data = response.json()          # convert fetched data to json file
        print(f"Bitcoin data: {data}")
    except Exception as e:
        print(f"Error! An error {e} was encountered.")
  
fetcher()