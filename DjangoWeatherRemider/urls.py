from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import never_cache
from django.contrib.staticfiles.views import serve
from DjangoWeatherRemider import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/users/', include('User.urls')),
    path('api/v1/cities/', include('City.urls')),
    path('api/v1/sublist/', include('Sublist.urls')),
]

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
