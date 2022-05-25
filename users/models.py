from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

from academic.validators import name_validator
from academic.options import *


# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(
        _("first name"),
        max_length=150,
        validators=[name_validator]
    )

    last_name = models.CharField(
        _("last name"),
        max_length=150,
        validators=[name_validator]
    )

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("Ya existe un usuario con esa dirección de correo."),
        },
    )

    user_image = models.ImageField(
        _("profile picture"),
        upload_to='assets/%Y/%m/%d',
        null=True,
        blank=True,
        help_text=_("Opcional. Foto de perfil del usuario."),
    )

    def __str__(self):
        return self.username


class HeadOfResearchProject(User):
    is_staff = False
    is_superuser = False
    pass


class HeadOfTeachingProject(User):
    is_staff = False
    is_superuser = False
    pass

"""
class State(models.Model):
    state_name = models.CharField(
        _("state name"),
        max_length=255,
        validators=[name_validator]
    )


class Municipality(models.Model):
    municipality_name = models.CharField(
        _("municipality name"),
        max_length=255,
        validators=[name_validator],
    )


class Locality(models.Model):
    locality_name = models.CharField(
        _("locality name"),
        max_length=255,
        validators=[name_validator],
    )
"""
