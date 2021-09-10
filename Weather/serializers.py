from rest_framework import serializers
from .models import WeatherApp


class WeatherAppSerializers(serializers.ModelSerializer):

    def get_fields(self):
        fields = super().get_fields()
        for field in fields.values():
            field.read_only = True
        return fields

    class Meta:
        model = WeatherApp
        fields = '__all__'


