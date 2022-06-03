from django.utils.translation import gettext_lazy as _
from django.db import models

from academic.validators import name_validator
from users.models import User

# Create your models here.


class Department(models.Model):
    department_name = models.CharField(
        _("department name"),
        max_length=255,
        unique=True,
        validators=[name_validator]
    )

    department_owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.department_name
