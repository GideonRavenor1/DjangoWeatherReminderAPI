from rest_framework import serializers
from .models import SubListApp
from User.serializers import UsersAppSerializers
from City.serializers import CitiesAppSerializers
from User.models import UserApp
from .exception import UserEmailNotFound


class SubListAppSerializers(serializers.ModelSerializer):
    user_id = UsersAppSerializers()
    city_id = CitiesAppSerializers()

    class Meta:
        model = SubListApp
        fields = '__all__'


class SubListAppAddSerializers(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        user = UserApp.objects.get(username=validated_data.get('user_id'))
        if user.email:
            instance = SubListApp.objects.create(**validated_data)
            return instance
        else:
            raise UserEmailNotFound

    def to_representation(self, instance):
        representation = super(SubListAppAddSerializers, self).to_representation(instance)
        representation['name'] = instance.city_id.name
        return representation

    class Meta:
        model = SubListApp
        fields = ('user_id', 'city_id', 'send_email')


class SubListAppAddAdminSerializers(serializers.ModelSerializer):

    class Meta:
        model = SubListApp
        fields = ('user_id', 'city_id', 'send_email')

    def create(self, validated_data):
        user = UserApp.objects.get(username=validated_data.get('user_id'))
        if user.email:
            instance = SubListApp.objects.create(**validated_data)
            return instance
        else:
            raise UserEmailNotFound

    def to_representation(self, instance):
        representation = super(SubListAppAddAdminSerializers, self).to_representation(instance)
        representation['username'] = instance.user_id.username
        representation['city'] = instance.city_id.name
        return representation



