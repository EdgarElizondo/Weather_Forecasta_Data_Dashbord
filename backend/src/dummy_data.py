import os
import requests

# CONSTANTS
API_KEY = os.getenv("API_WeatherMap")
MEASURE_TIME_INTERVAL = 3
CONVERSION_DAY_PARAMETER = int(24 / MEASURE_TIME_INTERVAL)


def get_data(place:str, days:int):
    # Get API Data
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    req = requests.get(url)
    data = req.json()
    filtered_data = data["list"][:days * CONVERSION_DAY_PARAMETER]
    
    return filtered_data

if __name__ == "__main__":
    get_data("Tokio", 3)