import requests
from rest_framework import serializers
from DjangoWeatherRemider import settings
from .models import CityApp
from Weather.models import WeatherApp
from Weather.serializers import WeatherAppSerializers
from rest_framework.exceptions import APIException


class CitiesAppSerializers(serializers.ModelSerializer):
    class Meta:
        model = CityApp
        fields = ["id", "name", "create_at"]


class CityAppSerializers(serializers.ModelSerializer):
    weather = WeatherAppSerializers()

    class Meta:
        model = CityApp
        fields = ['id', 'name', 'create_at', 'weather']


class CityCreateSerializers(serializers.ModelSerializer):
    weather = WeatherAppSerializers()

    def create(self, validated_data):
        url = settings.WEATHER_URL + settings.API_WEATHER
        city = validated_data.get('name')
        result = requests.get(url.format(city)).json()
        if result['cod'] == 200:
            update = validated_data.pop('weather')
            instance = CityApp.objects.create(**validated_data)
            WeatherApp.objects.create(temp=result['main']['temp'], feels_like=result['main']['feels_like'],
                                      pressure=result['main']['pressure'], visibility=result['visibility'],
                                      wind=result['wind']['speed'],
                                      icon=settings.ICON_URL.format(result['weather'][0]['icon']),
                                      city=CityApp.objects.get(name=city.capitalize()), update=update['update'])
            return instance
        else:
            raise ServiceUnavailable

    def to_representation(self, instance):
        representation = super(CityCreateSerializers, self).to_representation(instance)
        representation['weather'] = WeatherAppSerializers(instance.weather).data
        return representation

    class Meta:
        model = CityApp
        fields = ['id', 'name', 'weather', 'create_at']


class ServiceUnavailable(APIException):
    status_code = 404
    default_detail = 'City not found, try again.'
    default_code = 'City not found'
