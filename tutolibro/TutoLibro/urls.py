from django.urls import path
from .views import DeveloperList, DeveloperDetail

urlpatterns = [
    path("developers/", DeveloperList.as_view(), name="developer-list"),
    path("developers/<int:pk>/", DeveloperDetail.as_view(), name="developer-detail"),
]