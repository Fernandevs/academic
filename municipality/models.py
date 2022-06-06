from django.db import models
from django.utils.translation import gettext_lazy as _

from academic.validators import name_validator, number_validator
from state.models import State

# Create your models here.


class Municipality(models.Model):
    municipality_id = models.CharField(
        _('id municipality'),
        null=False,
        blank=False,
        max_length=3,
        validators=[number_validator],
        default='053'
    )

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
        default='16'
    )

    def __str__(self):
        return self.municipality_name
