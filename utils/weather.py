import requests
import datetime
import openmeteo_requests
from .config import CONFIG

URL = 'https://api.open-meteo.com/v1/forecast'
PARAMS = {
    "latitude": CONFIG['latitude'],
    "longitude": CONFIG['longitude'],
    "hourly": ["temperature_2m", "precipitation_probability", "precipitation"],
    "timezone": CONFIG['timezone'],
    "forecast_days": 1
}
openmeteo = openmeteo_requests.Client()


class WeatherData:
    temperature_2m: float = None
    precipitation_probability: float = None
    precipitation: float = None

    def __str__(self) -> str:
        return f"[{self.time}] Temperature: {self.temperature_2m}°C, Precipitation: {self.precipitation}mm, Probability: {self.precipitation_probability}%"


def get_wheater_data() -> list[WeatherData]:
    """
    Get weather from open meteo
    """
    response = openmeteo.weather_api(URL, PARAMS)[0]
    data = response.Hourly()
    result: list[WeatherData] = []

    for i in range(24):
        weatherData = WeatherData()
        weatherData.temperature_2m = data.Variables(0).Values(i)
        weatherData.precipitation_probability = data.Variables(1).Values(i)
        weatherData.precipitation = data.Variables(2).Values(i)
        result.append(weatherData)

    return result
