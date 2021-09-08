from rest_framework import serializers
from .models import UserApp


class UsersAppSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserApp
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'gender']


class UserAppSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserApp
        fields = ['id', 'username', 'email', 'first_name',
                  'last_name', 'gender', 'date_joined', 'last_login', 'is_staff',
                  'is_superuser']

