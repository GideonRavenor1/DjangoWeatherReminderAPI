from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    SubListAppView, SubListAppAddView,
    SubListAppAddAdminView, SubListAppDelete,
    SubListAppDeleteAdminView, SubListAppUserView
)


urlpatterns = [
    path('add', SubListAppAddView.as_view()),
    path('user_sublist/<int:pk>', SubListAppUserView.as_view()),
    path('add_admin', SubListAppAddAdminView.as_view()),
    path('delete/<int:pk>', SubListAppDelete.as_view()),
    path('delete_admin/<int:pk>', SubListAppDeleteAdminView.as_view()),

]

router = DefaultRouter()
router.register(r'', SubListAppView)

urlpatterns += router.urls


