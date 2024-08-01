# Retrieve data from a public API (e.g., OpenWeatherMap, JSONPlaceholder) and process it.
import requests

url = 'https://jsonplaceholder.typicode.com/posts/?userId=1'

response = requests.get(url)

data = response.json()

try:
    if response.status_code == 200:
        post = data[0]
        user_id = post['userId']
        title = post['title']
        body = post['body']

        print(user_id)
        print(title)
        print(body)
except Exception as e:
    print(f"Error {e} encountered!")