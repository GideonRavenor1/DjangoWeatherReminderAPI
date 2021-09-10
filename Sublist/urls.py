from django.urls import path
from .views import (
    SubListAppView, SubListAppAddView,
    SubListAppAddAdminView, SubListAppDelete,
    SubListAppDeleteAdminView
)


urlpatterns = [
    path('all', SubListAppView.as_view()),
    path('add', SubListAppAddView.as_view()),
    path('add_admin', SubListAppAddAdminView.as_view()),
    path('delete/<int:pk>', SubListAppDelete.as_view()),
    path('delete_admin/<int:pk>', SubListAppDeleteAdminView.as_view()),

]
