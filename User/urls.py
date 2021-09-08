from django.urls import path
from .views import UsersListView, UserView

urlpatterns = [
    path('all/', UsersListView.as_view()),
    path('<int:pk>/', UserView.as_view())
]