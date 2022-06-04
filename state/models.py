from django.db import models
from django.utils.translation import gettext_lazy as _

from academic.validators import name_validator, number_validator


# Create your models here.


class State(models.Model):
    state_id = models.CharField(
        _("id state"),
        primary_key=True,
        max_length=2,
        unique=True,
        error_messages={
            "unique": _("Ya existe un estado con ese identificador."),
        },
        null=False,
        blank=False,
        default='16',
        validators=[number_validator]
    )

    state_name = models.CharField(
        _("state"),
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        validators=[name_validator]
    )

    def __str__(self):
        return self.state_name
