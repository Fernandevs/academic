import datetime

from django.utils.translation import gettext_lazy as _
from django.db import models

from academic.options import DEGREE_OPTIONS, EGRESS_PERIOD
from careers.models import Career

# Create your models here.


class Egress(models.Model):
    id_number = models.CharField(
        _('id number'),
        max_length=9
    )

    student_name = models.CharField(
        _('name'),
        null=True,
        max_length=255
    )

    paternal_surname = models.CharField(
        _('paternal surname'),
        null=True,
        max_length=255
    )

    maternal_surname = models.CharField(
        _('maternal surname'),
        null=True,
        max_length=255
    )

    career = models.ForeignKey(
        to=Career,
        on_delete=models.CASCADE
    )

    option = models.PositiveSmallIntegerField(
        _('option'),
        choices=DEGREE_OPTIONS
    )

    egress_period = models.PositiveSmallIntegerField(
        _('egress period'),
        choices=EGRESS_PERIOD
    )

    egress_year = models.DateField(
        _('egress_year'),
        default=datetime.datetime.now().year
    )

    """
    plan = models.CharField(
        _('plan'),
        max_length=255
    )

    graduation_period = models.CharField(
        _('graduation period'),
        max_length=255
    )

    graduation_year = models.DateField(
        _('graduation year'),
        default=datetime.datetime.now().year
    )

    option = models.PositiveSmallIntegerField(
        _('option'),
        choices=DEGREE_OPTIONS
    )

    degree_date = models.DateField(
        _('degree date'),
        default=datetime.date
    )

    egress_date = models.DateField(
        _('egress date'),
        default=datetime.date
    )
"""

    def __str__(self):
        return self.student_name
