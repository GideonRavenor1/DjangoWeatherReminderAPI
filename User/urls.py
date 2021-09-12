from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    UsersListView,
    UserDeleteView, UserUpdateView,
    UserUpdateDestroyAdminView, UserCreateAdminView
)

urlpatterns = [
    path('delete/<int:pk>', UserDeleteView.as_view()),
    path('update/<int:pk>', UserUpdateView.as_view()),
    path('delete_update_admin/<int:pk>', UserUpdateDestroyAdminView.as_view()),
    path('create_admin', UserCreateAdminView.as_view())

]

router = DefaultRouter()
router.register(r'', UsersListView)

urlpatterns += router.urls
