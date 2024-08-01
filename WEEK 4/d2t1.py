# Fetch weather data from a weather API and display it.

import requests

api_key = "93c89478c56945f0900f813f1fcdeeff"
city = 'Raleigh'
url = f'https://api.weatherbit.io/v2.0/current?city={city}&key={api_key}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    weather_data = data['data'][0]
    temperature = weather_data['temp']
    weather = weather_data['weather']['description']
    print(f'Temperature: {temperature}')
    print(f'Weather: {weather}')
else:
    print('City not found')

# data = {
#     'count': 1, 
#     'data': [
#         {
#             'app_temp': 33.1, 'aqi': 50, 'city_name': 'Raleigh', 'clouds': 0, 'country_code': 'US', 'datetime': '2024-08-01:12', 'dewpt': 24, 'dhi': 91, 'dni': 760, 'elev_angle': 30.07, 'ghi': 466, 'gust': None, 'h_angle': -64.3, 'lat': 35.7721, 'lon': -78.63861, 'ob_time': '2024-08-01 12:40', 'pod': 'd', 'precip': 0, 'pres': 1005.9, 'rh': 76, 'slp': 1018.6, 'snow': 0, 'solar_rad': 466, 'sources': ['1327W', 'radar', 'satellite'], 'state_code': 'NC', 'station': '1327W', 'sunrise': '10:23', 'sunset': '00:18', 'temp': 28.7, 'timezone': 'America/New_York', 'ts': 1722516000, 'uv': 3, 'vis': 13, 'weather': {'icon': 'c01d', 'description': 'Clear sky', 'code': 800}, 'wind_cdir': 'WNW', 'wind_cdir_full': 'west-northwest', 'wind_dir': 284, 'wind_spd': 0.9
#             }
#             ]
#  }