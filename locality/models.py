from django.db import models
from django.utils.translation import gettext_lazy as _

from academic.validators import name_validator, number_validator
from municipality.models import Municipality
from state.models import State

# Create your models here.


class Locality(models.Model):
    locality_id = models.CharField(
        _('id locality'),
        primary_key=True,
        unique=False,
        null=False,
        blank=False,
        max_length=4,
        validators=[number_validator],
        default='0001'
    )

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
        default='053'
    )

    state = models.ForeignKey(
        State,
        models.CASCADE,
        default='16'
    )

    def __str__(self):
        return self.locality_name
