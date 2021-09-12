import requests
from django.http import QueryDict
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from DjangoWeatherRemider import settings
from .models import CityApp
from .services import update_weather
from .permissions import IsAdminUserOrReadOnly
from .serializers import (
    CitiesAppSerializers, CityAppGetDeleteSerializers,
    CityCreateSerializers
)


class CitiesListView(generics.ListAPIView):
    queryset = CityApp.objects.all()
    serializer_class = CitiesAppSerializers
    permission_classes = (IsAuthenticated,)


class CityDetailView(generics.RetrieveDestroyAPIView):
    queryset = CityApp.objects.all()
    serializer_class = CityAppGetDeleteSerializers
    permission_classes = (IsAdminUserOrReadOnly, IsAuthenticated)

    def get(self, request, *args, **kwargs):
        url = settings.WEATHER_URL + settings.API_WEATHER
        city = CityApp.objects.get(pk=kwargs['pk']).name
        result = requests.get(url.format(city)).json()
        update_weather(result, kwargs)

        return self.retrieve(request, *args, **kwargs)


class CityCreateView(generics.ListCreateAPIView):
    queryset = CityApp.objects.all()
    serializer_class = CityCreateSerializers
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, QueryDict):
            request.data._mutable = True
            request.data['name'] = request.data['name'].title()
            request.data._mutable = False
        else:
            request.data['name'] = request.data['name'].title()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
