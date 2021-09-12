from City.models import CityApp
from DjangoWeatherRemider import settings
from Weather.models import WeatherApp


def update_weather(result, kwargs):
    WeatherApp.objects.filter(city=kwargs['pk']).update(temp=result['main']['temp'],
                                                        feels_like=result['main']['feels_like'],
                                                        pressure=result['main']['pressure'],
                                                        visibility=result['visibility'],
                                                        wind=result['wind']['speed'],
                                                        icon=settings.ICON_URL.format(result['weather'][0]['icon']))


def create_weather(result, city):
    WeatherApp.objects.create(temp=result['main']['temp'], feels_like=result['main']['feels_like'],
                              pressure=result['main']['pressure'], visibility=result['visibility'],
                              wind=result['wind']['speed'],
                              icon=settings.ICON_URL.format(result['weather'][0]['icon']),
                              city=CityApp.objects.get(name=city))
