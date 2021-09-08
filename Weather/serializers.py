from rest_framework import serializers
from .models import WeatherApp


class WeatherAppSerializers(serializers.ModelSerializer):
    class Meta:
        model = WeatherApp
        read_only_fields = ['temp', 'feels_like', 'pressure', 'visibility', 'wind', 'icon']
        fields = ['update', 'temp', 'feels_like', 'pressure', 'visibility', 'wind', 'icon']
