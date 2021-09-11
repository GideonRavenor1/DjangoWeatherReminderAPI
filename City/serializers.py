import requests
from rest_framework import serializers
from DjangoWeatherRemider import settings
from .exceptions import CityNotFound
from .models import CityApp
from Weather.models import WeatherApp
from Weather.serializers import WeatherAppSerializers


class CitiesAppSerializers(serializers.ModelSerializer):
    weather = WeatherAppSerializers(many=True)

    class Meta:
        model = CityApp
        fields = ("id", "name", "create_at", "weather")


class CityAppGetDeleteSerializers(serializers.ModelSerializer):
    weather = WeatherAppSerializers(many=True)

    class Meta:
        model = CityApp
        fields = ('id', 'name', 'create_at', 'weather')


class CityCreateSerializers(serializers.ModelSerializer):
    weather = WeatherAppSerializers(many=True, read_only=True)

    def create(self, validated_data):
        url = settings.WEATHER_URL + settings.API_WEATHER
        city = validated_data.get('name')
        result = requests.get(url.format(city)).json()
        if result['cod'] == 200:
            instance = CityApp.objects.get_or_create(**validated_data)
            WeatherApp.objects.create(temp=result['main']['temp'], feels_like=result['main']['feels_like'],
                                      pressure=result['main']['pressure'], visibility=result['visibility'],
                                      wind=result['wind']['speed'],
                                      icon=settings.ICON_URL.format(result['weather'][0]['icon']),
                                      city=CityApp.objects.get(name=city))
            return instance[0]
        else:
            raise CityNotFound

    class Meta:
        model = CityApp
        fields = ('id', 'name', 'create_at', 'weather')
