from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from .models import SubListApp
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    SubListAppSerializers, SubListAppAddSerializers,
    SubListAppAddAdminSerializers
)


class SubListAppView(viewsets.GenericViewSet):
    queryset = SubListApp.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = SubListAppSerializers

    def list(self, request):
        page = self.paginate_queryset(self.queryset)
        serializer = SubListAppSerializers(page, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = SubListAppSerializers(user)
        return Response(serializer.data)


class SubListAppUserView(generics.ListAPIView):
    serializer_class = SubListAppSerializers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return SubListApp.objects.none()
        return SubListApp.objects.filter(user_id=self.kwargs['pk'])


class SubListAppAddView(generics.CreateAPIView):
    queryset = SubListApp.objects.all()
    serializer_class = SubListAppAddSerializers
    permission_classes = (IsAuthenticated,)


class SubListAppAddAdminView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = SubListApp.objects.all()
    serializer_class = SubListAppAddAdminSerializers


class SubListAppDelete(generics.RetrieveDestroyAPIView):
    queryset = SubListApp.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)
    serializer_class = SubListAppSerializers


class SubListAppDeleteAdminView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = SubListApp.objects.all()
    serializer_class = SubListAppSerializers
