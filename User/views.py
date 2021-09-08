from rest_framework import generics
from rest_framework.response import Response
from .models import UserApp
from .serializers import UsersAppSerializers, UserAppSerializers


class UsersListView(generics.ListAPIView):
    queryset = UserApp.objects.all()
    serializer_class = UsersAppSerializers


class UserView(generics.RetrieveAPIView):
    queryset = UserApp.objects.all()
    serializer_class = UserAppSerializers

