import requests
import json
import os
import pandas as pd

def fetch_data(city):
    token = "04b86b65d4fb7a1db07baadc0709384f352fdf46"
    url = f"https://api.waqi.info/feed/{city}/?token={token}"
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'ok':
        aqi = data['data']['aqi']
        forecast = data['data']['forecast']['daily']
        weather_data = {
            'city': city,
            'aqi': aqi,
            'forecast': forecast
        }
        return weather_data
    else:
        raise Exception("Error fetching data")

def save_data(data, filename):
    file_path = os.path.join("data", filename)
    with open(file_path, 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    city = "bengaluru"
    data = fetch_data(city)
    save_data(data, "weather_data.json")
