from rest_framework.generics import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import UserApp
from .permissions import IsUserOrReadOnly
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import (
    UsersAppSerializers, UserAppSerializers,
    UserAppUpdateSerializers, UserAppCreateAdmin
)


class UsersListView(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = UserApp.objects.all()
    serializer_class = UserAppSerializers

    def list(self, request):
        page = self.paginate_queryset(self.queryset)
        serializer = UsersAppSerializers(page, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = UserAppSerializers(user)
        return Response(serializer.data)


class UserDeleteView(generics.RetrieveDestroyAPIView):
    queryset = UserApp.objects.all()
    serializer_class = UserAppSerializers
    permission_classes = (IsUserOrReadOnly, IsAuthenticated)


class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UserApp.objects.all()
    serializer_class = UserAppUpdateSerializers
    permission_classes = (IsUserOrReadOnly, IsAuthenticated)


class UserUpdateDestroyAdminView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserApp.objects.all()
    serializer_class = UserAppUpdateSerializers
    permission_classes = (IsAdminUser,)


class UserCreateAdminView(generics.CreateAPIView):
    serializer_class = UserAppCreateAdmin
    permission_classes = (IsAdminUser,)

