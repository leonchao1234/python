import requests
import datetime
import os
import sys

os.chdir(sys.path[0])
api_key = "892da2f13edf3c7f382637760e72d224"
base_url = "https://api.openweathermap.org/data/2.5/onecall?"
lon = "121.5319"
lat = "25.0478"
exclude = "minutely,hourly"
units = "metric"
lang = "zh_tw"

send_url = base_url
send_url += "lat=" + lat
send_url += "&lon=" + lon
send_url += "&exclude=" + exclude
send_url += "&appid=" + api_key
send_url += "&units=" + units
send_url += "&lang=" + lang

print(send_url)
response = requests.get(send_url)
info = response.json()

if "daily" in info.keys():
    for i in range(7):
        temp = info["daily"][i]["temp"]["day"]
        time = datetime.datetime.fromtimestamp(
            info["daily"][i]["dt"]).strftime("%m/%d")
        print(f"{time}的溫度是{temp}度")
else:
    print("Request Fail")
