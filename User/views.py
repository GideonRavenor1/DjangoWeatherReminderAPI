from rest_framework import generics
from .models import UserApp
from .permissions import IsUserOrReadOnly
from rest_framework.permissions import IsAdminUser
from .serializers import (
    UsersAppSerializers, UserAppSerializers,
    UserAppUpdateSerializers, UserAppCreateAdmin
)


class UsersListView(generics.ListAPIView):
    queryset = UserApp.objects.all()
    serializer_class = UsersAppSerializers


class UserView(generics.RetrieveAPIView):
    queryset = UserApp.objects.all()
    serializer_class = UserAppSerializers


class UserDeleteView(generics.RetrieveDestroyAPIView):
    queryset = UserApp.objects.all()
    serializer_class = UserAppSerializers
    permission_classes = (IsUserOrReadOnly,)


class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UserApp.objects.all()
    serializer_class = UserAppUpdateSerializers
    permission_classes = (IsUserOrReadOnly,)


class UserUpdateDestroyAdminView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserApp.objects.all()
    serializer_class = UserAppUpdateSerializers
    permission_classes = (IsAdminUser,)


class UserCreateAdminView(generics.CreateAPIView):
    serializer_class = UserAppCreateAdmin
    permission_classes = (IsAdminUser,)

