from rest_framework import generics
from .models import UserApp
from .permissions import IsUserOrReadOnly
from .serializers import (
    UsersAppSerializers, UserAppSerializers,
    UserAppUpdateSerializers
)


class UsersListView(generics.ListAPIView):
    queryset = UserApp.objects.all()
    serializer_class = UsersAppSerializers


class UserView(generics.RetrieveDestroyAPIView):
    queryset = UserApp.objects.all()
    serializer_class = UserAppSerializers


class UserDeleteView(generics.RetrieveDestroyAPIView):
    queryset = UserApp.objects.all()
    serializer_class = UserAppSerializers


class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UserApp.objects.all()
    serializer_class = UserAppUpdateSerializers
    permission_classes = [IsUserOrReadOnly]


