from django.utils.translation import gettext_lazy as _
from django.db import models

from academic.validators import name_validator

# Create your models here.


class Career(models.Model):
    career = models.CharField(
        _("career"),
        max_length=255,
        unique=True,
        error_messages={
            "unique": _("Ya existe esta carrera."),
        },
        null=False,
        blank=False,
        validators=[name_validator]
    )

    is_active = models.BooleanField(
        _("is active"),
        default=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.career
