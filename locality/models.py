from django.db import models
from django.utils.translation import gettext_lazy as _

from academic.validators import name_validator
from municipality.models import Municipality

# Create your models here.


class Locality(models.Model):
    locality_name = models.CharField(
        _("locality"),
        max_length=255,
        null=False,
        blank=False,
        validators=[name_validator]
    )

    municipality = models.ForeignKey(
        Municipality,
        models.CASCADE,
    )

    def __str__(self):
        return self.locality_name
