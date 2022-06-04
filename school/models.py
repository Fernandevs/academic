from django.utils.translation import gettext_lazy as _
from django.db import models

from academic.options import REG_PROC, MOD_BAC

# Create your models here.


class School(models.Model):
    cve_proc = models.CharField(
        _('Clave'),
        primary_key=True,
        unique=True,
        error_messages={
            "unique": _("Ya existe una escuela con esa clave."),
        },
        null=False,
        blank=False,
        max_length=6,
        default='000000'
    )  # Clave de la institución en la que concluyó sus estudios de bachillerato

    nom_proc = models.CharField(
        _('Nombre completo de la institución donde concluyó el nivel medio superior'),
        null=True,
        blank=True,
        max_length=130,
    )  # Nombre completo de la institución donde concluyó el nivel medio superior

    ciu_proc = models.CharField(
        _('Ciudad donde se ubica la institución'),
        null=True,
        blank=True,
        max_length=50
    )
    # Nombre de la ciudad donde se ubica la institución en la que concluyó el nivel medio superior;
    # si fue en el extranjero indique el país

    reg_proc = models.CharField(
        _('Régimen de sostenimiento'),
        null=False,
        blank=False,
        max_length=1,
        choices=REG_PROC,
        default='1'
    )
    # ¿Cuál es el régimen de sostenimiento de la escuela en la que estudió el último año
    # del nivel medio superior?

    mod_bac = models.CharField(
        _('modalidad'),
        null=False,
        blank=False,
        max_length=1,
        choices=MOD_BAC,
        default='1'
    )  # ¿En qué modalidad obtuvo su certificado del bachillerato?

    """
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
"""