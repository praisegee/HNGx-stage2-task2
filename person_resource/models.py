from django.db import models
from django.utils.translation import gettext as _


class Person(models.Model):
    name = models.CharField(_("Name"), max_length=50)

    def __str__(self) -> str:
        return self.name
