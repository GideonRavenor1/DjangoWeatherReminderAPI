from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import SubListApp
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    SubListAppSerializers, SubListAppAddSerializers,
    SubListAppAddAdminSerializers
)


class SubListAppView(generics.ListAPIView):
    queryset = SubListApp.objects.all()
    serializer_class = SubListAppSerializers


class SubListAppAddView(generics.CreateAPIView):
    queryset = SubListApp.objects.all()
    serializer_class = SubListAppAddSerializers


class SubListAppAddAdminView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = SubListApp.objects.all()
    serializer_class = SubListAppAddAdminSerializers


class SubListAppDelete(generics.RetrieveDestroyAPIView):
    queryset = SubListApp.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SubListAppSerializers


class SubListAppDeleteAdminView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = SubListApp.objects.all()
    serializer_class = SubListAppSerializers
