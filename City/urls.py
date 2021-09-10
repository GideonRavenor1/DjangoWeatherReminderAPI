from django.urls import path
from .views import CitiesListView, CityView, CityCreateView

urlpatterns = [
    path('all', CitiesListView.as_view()),
    path('detail/<int:pk>', CityView.as_view()),
    path('add', CityCreateView.as_view()),
]