from django.urls import path
from .views import (
    UsersListView, UserView,
    UserDeleteView, UserUpdateView,
    UserUpdateDestroyAdminView, UserCreateAdminView
)

urlpatterns = [
    path('all', UsersListView.as_view()),
    path('<int:pk>', UserView.as_view()),
    path('delete/<int:pk>', UserDeleteView.as_view()),
    path('update/<int:pk>', UserUpdateView.as_view()),
    path('delete_update_admin/<int:pk>', UserUpdateDestroyAdminView.as_view()),
    path('create_admin', UserCreateAdminView.as_view())

]
