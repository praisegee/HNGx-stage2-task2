from rest_framework.viewsets import ModelViewSet

from .models import Person
from .serializers import PersonSerializer


class PersonAPI(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_url_kwarg = "user_id"
