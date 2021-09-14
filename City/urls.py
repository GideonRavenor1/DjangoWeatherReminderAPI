from django.urls import path
from .views import CitiesListView, CityDetailView, CityCreateView

app_name = 'City'

urlpatterns = [
    path('all', CitiesListView.as_view(), name='all_cities'),
    path('detail/<int:pk>', CityDetailView.as_view(), name='detail_city'),
    path('add', CityCreateView.as_view(), name='add_city'),
]