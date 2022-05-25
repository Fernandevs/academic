from django.utils.translation import gettext_lazy as _
from django.db import models

from academic.validators import name_validator

# Create your models here.


class School(models.Model):
    school_name = models.CharField(
        _("school name"),
        max_length=255,
        validators=[name_validator]
    )

    catchword = models.CharField(
        _("catchword"),
        max_length=255,
        validators=[name_validator]
    )

    logo = models.ImageField(
        _("school logo"),
        upload_to='assets/school/%Y/%m/%d',
        null=False,
        blank=False,
        help_text=_("Obligatoria. Logo de la escuela."),
    )

    level = models.CharField(
        _("level"),
        max_length=255,
        validators=[name_validator]
    )

    control = models.CharField(
        _("control"),
        max_length=255,
        validators=[name_validator]
    )

    clue = models.CharField(
        _("clue"),
        max_length=255,
        validators=[name_validator]
    )

    sustenance = models.CharField(
        _("sustenance"),
        max_length=255,
        validators=[name_validator]
    )

    location = models.CharField(
        _("location"),
        max_length=255,
        validators=[name_validator]
    )

    municipality = models.CharField(
        _("municipality"),
        max_length=255,
        validators=[name_validator]
    )

    student_population = models.PositiveIntegerField(
        _("student population"),
    )

    teaching_population = models.PositiveIntegerField(
        _("teaching population"),
    )

    def __str__(self):
        return self.school_name
