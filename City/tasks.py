import requests
from DjangoWeatherRemider import settings
from DjangoWeatherRemider.celery import app
from .models import CityApp
from .services import update_weather
URL = settings.WEATHER_URL + settings.API_WEATHER


@app.task
def constant_weather_update_every_one_hour():
    cities = CityApp.objects.all()
    if not cities:
        return 'Cities not found'
    for city in cities:
        result = requests.get(URL.format(city.name)).json()
        update_weather(result, {'pk': city.pk})
    return 'Successfully'
