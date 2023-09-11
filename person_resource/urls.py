from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PersonAPI

router = DefaultRouter(trailing_slash=False)
router.register("", PersonAPI, basename="person")

urlpatterns = [path("", include(router.urls))]
