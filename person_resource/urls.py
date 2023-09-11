from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PersonAPI

router = DefaultRouter()
router.register("", PersonAPI, basename="person")

urlpatterns = [path(r"api/?", include(router.urls))]
