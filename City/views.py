import requests
from rest_framework import generics, status
from rest_framework.response import Response
from DjangoWeatherRemider import settings
from .models import CityApp
from Weather.models import WeatherApp
from .serializers import (
    CitiesAppSerializers, CityAppGetDeleteSerializers,
    CityCreateSerializers
)


class CitiesListView(generics.ListAPIView):
    queryset = CityApp.objects.all()
    serializer_class = CitiesAppSerializers


class CityView(generics.RetrieveDestroyAPIView):
    queryset = CityApp.objects.all()
    serializer_class = CityAppGetDeleteSerializers

    def get(self, request, *args, **kwargs):
        url = settings.WEATHER_URL + settings.API_WEATHER
        city = CityApp.objects.get(pk=kwargs['pk']).name
        result = requests.get(url.format(city)).json()
        WeatherApp.objects.filter(city=kwargs['pk']).update(temp=result['main']['temp'],
                                                            feels_like=result['main']['feels_like'],
                                                            pressure=result['main']['pressure'],
                                                            visibility=result['visibility'],
                                                            wind=result['wind']['speed'],
                                                            icon=settings.ICON_URL.format(result['weather'][0]['icon']))

        return self.retrieve(request, *args, **kwargs)


class CityCreateView(generics.ListCreateAPIView):
    queryset = CityApp.objects.all()
    serializer_class = CityCreateSerializers

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['name'] = request.data['name'].title()
        request.data._mutable = False
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
