from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    UsersListView,
    UserDeleteView, UserUpdateView,
    UserUpdateDestroyAdminView, UserCreateAdminView
)

app_name = 'User'

urlpatterns = [
    path('delete/<int:pk>', UserDeleteView.as_view(), name='delete_user'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='update_user'),
    path('delete_update_admin/<int:pk>', UserUpdateDestroyAdminView.as_view(), name='delete_updateAdmin_user'),
    path('create_admin', UserCreateAdminView.as_view(), name='createAdmin_user')

]

router = DefaultRouter()
router.register(r'', UsersListView)

urlpatterns += router.urls
