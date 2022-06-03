from django.db import models
from django.utils.translation import gettext_lazy as _

from academic.validators import name_validator

# Create your models here.


class State(models.Model):
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
