import os
import requests
from dotenv import load_dotenv
from state import SecretaryState

load_dotenv()

def check_weather(state: SecretaryState) -> SecretaryState:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    city = "Coppell"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200:
            desc = data["weather"][0]["description"].capitalize()
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            summary = f"{desc}, {temp}°F, feels like {feels_like}°F, humidity {humidity}%, wind {wind} mph"
        else:
            summary = f"Weather API error: {data.get('message', 'Unknown error')}"
    except Exception as e:
        summary = f"Weather fetch failed: {str(e)}"

    return state.copy(update={"weather": summary})