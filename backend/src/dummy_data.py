import os
import requests

# API KEY
#API_KEY = os.getenv("f008cfcf53ef01d493df6bc5ac3d76c3")
API_KEY = "f008cfcf53ef01d493df6bc5ac3d76c3"

def get_data(place:str, days:int, kind:str):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    req = requests.get(url)

    dates = ["2022-25-10","2022-26-10","2022-27-10"]
    temperatures = [10, 11, 15]

    print(req.json())

    return dates, temperatures

if __name__ == "__main__":
    get_data("Tokio", 1, "Sky")