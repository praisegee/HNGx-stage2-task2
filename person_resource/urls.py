from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PersonAPI

router = DefaultRouter()
router.register("", PersonAPI, basename="person")

urlpatterns = [path("api/", include(router.urls))]
