from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _
from django.db import models

from academic.validators import name_validator

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

    groups = models.ForeignKey(
        Group,
        models.CASCADE,
        _('role'),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username
