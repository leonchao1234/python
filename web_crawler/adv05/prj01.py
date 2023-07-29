import requests

import os
import sys

os.chdir(sys.path[0])
api_key = "b4ccba82e413dab0d5670f051a0f09c1"
base_url = "https://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name:")
units = "metric"
lang = "zh_tw"

send_url = base_url
send_url += "appid=" + api_key
send_url += "&q=" + city_name
send_url += "&units=" + units
send_url += "&lang=" + lang
print(send_url)
response = requests.get(send_url)
info = response.json()
print(info)
print(f'city = {info["name"]}')
print(f'temp = {info["main"]["temp"]}')
print(f'description = {info["weather"][0]["description"]}')

if "main" in info.keys():
    icon_code = info["weather"][0]["icon"]
    icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
    response = requests.get(icon_url)
    with open(f"{icon_code}.png", "wb") as icon_file:
        icon_file.write(response.content)
else:
    print("City Not Found")
