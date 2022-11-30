import requests

OWN_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
API_KEY = "ad82e5277ecd614bbd9bb16810968840"


class Weather:
    """
    This class is used to show the weather in the next 12 hours.
    :parameter lat: latitude
    :parameter lon: longitude
    """

    def __init__(self, lat: float = 13.756331, lon: float = 100.501762):
        self.__lon = lon
        self.__lat = lat

    @property
    def lon(self):
        """Return the longitude."""
        return self.__lon

    @lon.setter
    def lon(self, new_lon):
        """Change the longitude."""
        self.__lon = new_lon

    @property
    def lat(self):
        """Return the latitude."""
        return self.__lat

    @lat.setter
    def lat(self, new_lat):
        """Change the latitude."""
        self.__lat = new_lat

    def get_weather(self) -> list:
        """Show the weather in the next 12 hours."""
        weather_params = {
            "lat": self.lat,
            "lon": self.lon,
            "appid": API_KEY,
            "exclude": "current,minutely,daily"
        }

        response = requests.get(OWN_ENDPOINT, params=weather_params, timeout=5)
        weather_data = response.json()
        weather_slice = weather_data["hourly"][:12]
        _list = []
        will_rain = False

        for index, hour_data in enumerate(weather_slice):
            condition_code = hour_data["weather"][0]["id"]

            if int(condition_code) < 700:
                _list.append(f"It is going to rain in {index + 1} hours.")
                will_rain = True
            else:
                _list.append(f"It is not going to rain in {index + 1} hours.")

        if will_rain:
            _list.append("Bring an umbrella with you today.")
        else:
            _list.append(
                "No need to bring an umbrella, There is no rain in 12 hours.")
        return _list
