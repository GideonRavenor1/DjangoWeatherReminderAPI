from django.urls import path
from .views import CitiesListView, CityView, CityCreateView

urlpatterns = [
    path('all/', CitiesListView.as_view()),
    path('<int:pk>/', CityView.as_view()),
    path('create/', CityCreateView.as_view())
]