from django.urls import path
from .views import CitiesListView, CityDetailView, CityCreateView

urlpatterns = [
    path('all', CitiesListView.as_view()),
    path('detail/<int:pk>', CityDetailView.as_view()),
    path('add', CityCreateView.as_view()),
]