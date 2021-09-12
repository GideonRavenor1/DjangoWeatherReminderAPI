from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .yasg import urlpatterns as dict_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/token', obtain_auth_token, name='token'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/users/', include('User.urls')),
    path('api/v1/cities/', include('City.urls')),
    path('api/v1/sublist/', include('Sublist.urls')),
]

urlpatterns += dict_urls
