import os
import requests

# CONSTANTS
API_KEY = os.getenv("API_WeatherMap")
MEASURE_TIME_INTERVAL = 3
CONVERSION_DAY_PARAMETER = int(24 / MEASURE_TIME_INTERVAL)


def get_data(place:str, days:int, kind:str):
    # Get API Data    
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    req = requests.get(url)

    dates = ["2022-25-10","2022-26-10","2022-27-10"]
    weather = [10, 11, 15]

    data = []
    json_data = req.json()
    if kind == "Temperature":
        data = [json_data["list"][day]["main"]["temp"]/10 for day in range(days * CONVERSION_DAY_PARAMETER)]
    elif kind == "Sky":
        data = [json_data["list"][day]["weather"][0]["main"] for day in range(days * CONVERSION_DAY_PARAMETER)]

    print(data)
    return dates, weather

if __name__ == "__main__":
    get_data("Tokio", 1, "Sky")