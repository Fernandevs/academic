from django.db import models
from django.utils.translation import gettext_lazy as _

from academic.validators import name_validator
from state.models import State

# Create your models here.


class Municipality(models.Model):
    municipality_name = models.CharField(
        _("municipality"),
        max_length=255,
        null=False,
        blank=False,
        validators=[name_validator]
    )

    state = models.ForeignKey(
        State,
        models.CASCADE,
    )

    def __str__(self):
        return self.municipality_name
