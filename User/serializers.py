from rest_framework import serializers, permissions
from .models import UserApp


class UsersAppSerializers(serializers.ModelSerializer):
    subscriptions = serializers.IntegerField(
        source='subscriptions.count',
        read_only=True
    )

    class Meta:
        model = UserApp
        fields = ['id', 'username', 'email', 'first_name',
                  'last_name', 'gender', 'subscriptions']


class UserAppSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserApp
        fields = ['id', 'username', 'email', 'first_name',
                  'last_name', 'gender', 'date_joined', 'last_login',
                  'is_staff', 'is_superuser', 'subscriptions']


class UserAppUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserApp
        fields = ['id', 'username', 'email',
                  'first_name', 'last_name', 'gender']

