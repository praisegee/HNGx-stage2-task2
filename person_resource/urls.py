from django.urls import include, path

from .routers import OptionalSlashRouter
from .views import PersonAPI

router = OptionalSlashRouter()
router.register("", PersonAPI, basename="person")

urlpatterns = [path("api/", include(router.urls))]
