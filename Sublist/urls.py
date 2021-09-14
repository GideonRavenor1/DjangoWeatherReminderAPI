from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    SubListAppView, SubListAppAddView,
    SubListAppAddAdminView, SubListAppDelete,
    SubListAppDeleteAdminView, SubListAppUserView
)

app_name = 'Sublist'

urlpatterns = [
    path('add', SubListAppAddView.as_view(), name='add_subscription'),
    path('user_sublist/<int:pk>', SubListAppUserView.as_view(), name='user_subscription'),
    path('add_admin', SubListAppAddAdminView.as_view(), name='addAdmin_subscription'),
    path('delete/<int:pk>', SubListAppDelete.as_view(), name='delete_subscription'),
    path('delete_admin/<int:pk>', SubListAppDeleteAdminView.as_view(), name='deleteAdmin_subscription'),

]

router = DefaultRouter()
router.register(r'', SubListAppView)

urlpatterns += router.urls


