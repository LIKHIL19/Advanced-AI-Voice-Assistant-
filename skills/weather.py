# File: skills/weather.py

import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY", "")

def get_weather(city: str) -> str:
    """
    Fetch current weather for the given city.
    Returns a human friendly string or an error message.
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    resp = requests.get(url, params=params)
    data = resp.json()

    # Check for errors
    if data.get("cod") != 200:
        # OpenWeather returns e.g. {"cod":"404","message":"city not found"}
        return f"Could not fetch weather for '{city}': {data.get('message', 'Unknown error')}."

    # Extract the fields safely
    weather_list = data.get("weather", [])
    main = data.get("main", {})

    if not weather_list or "description" not in weather_list[0] or "temp" not in main:
        return f"Unexpected response format for '{city}'."

    desc = weather_list[0]["description"]
    temp = main["temp"]
    return f"The weather in {city.title()} is {desc} at {temp:.1f}°C."