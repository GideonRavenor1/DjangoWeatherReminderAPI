from rest_framework import serializers
from .models import SubListApp


class SubListAppSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubListApp
        fields = '__all__'
