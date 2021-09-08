from rest_framework import generics
from rest_framework.response import Response
from .models import CityApp
from .serializers import CitiesAppSerializers, CityAppSerializers, CityCreateSerializers, ServiceUnavailable
from Weather.models import WeatherApp
from DjangoWeatherRemider import settings
import requests


class CitiesListView(generics.ListAPIView):
    queryset = CityApp.objects.all()
    serializer_class = CitiesAppSerializers


class CityView(generics.RetrieveAPIView):
    queryset = CityApp.objects.all()
    serializer_class = CityAppSerializers


class CityCreateView(generics.CreateAPIView):
    queryset = WeatherApp.objects.all()
    serializer_class = CityCreateSerializers

    '''def perform_create(self, serializer):
        url = settings.WEATHER_URL + settings.API_WEATHER
        city = self.request.data.get('name')
        result = requests.get(url.format(city)).json()
        if result['cod'] == 200:
            serializer.save()
            WeatherApp.objects.create(temp=result['main']['temp'], feels_like=result['main']['feels_like'],
                                      pressure=result['main']['pressure'], visibility=result['visibility'],
                                      wind=result['wind']['speed'],
                                      icon=settings.ICON_URL.format(result['weather'][0]['icon']),
                                      city=CityApp.objects.get(name=city.capitalize()))

        else:
            raise ServiceUnavailable'''
