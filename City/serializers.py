import requests
from rest_framework import serializers
from DjangoWeatherRemider import settings
from .exceptions import CityNotFound
from .models import CityApp
from Weather.serializers import WeatherAppSerializers
from .services import create_weather


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
            create_weather(result, city)
            return instance[0]
        else:
            raise CityNotFound

    class Meta:
        model = CityApp
        fields = ('id', 'name', 'create_at', 'weather')
