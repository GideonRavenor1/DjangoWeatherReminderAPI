from rest_framework import serializers
from .models import UserApp


class UsersAppSerializers(serializers.ModelSerializer):
    subscriptions = serializers.IntegerField(
        source='subscriptions.count',
        read_only=True
    )

    class Meta:
        model = UserApp
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'gender', 'subscriptions')


class UserAppSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserApp
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'gender', 'date_joined', 'last_login',
                  'is_staff', 'is_superuser', 'subscriptions')


class UserAppUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserApp
        fields = ('id', 'username', 'email',
                  'first_name', 'last_name', 'gender')


class UserAppCreateAdmin(serializers.ModelSerializer):

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = UserApp
        fields = ('username', 'email', 'password', 'first_name',
                  'last_name', 'gender',
                  'is_staff')

