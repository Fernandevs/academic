import datetime

from django.utils.translation import gettext_lazy as _
from django.db import models

from academic.options import SEX
from academic.validators import name_validator

from careers.models import Career

# Create your models here.


class Student(models.Model):
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

    career = models.ForeignKey(
        to=Career,
        on_delete=models.CASCADE
    )

    plan = models.CharField(
        _('plan'),
        max_length=255
    )

    period = models.CharField(
        _('period'),
        max_length=255
    )

    year = models.DateField(
        _('year'),
        default=datetime.datetime.now().year
    )

    record_number = models.PositiveIntegerField(
        _('record number'),
    )

    control_number = models.CharField(
        _('control_number'),
        max_length=8
    )

    school_of_origin = models.CharField(
        _('school_of_origin'),
        max_length=255
    )

    average = models.DecimalField(
        _('average'),
        max_digits=4,
        decimal_places=2
    )

    place_of_origin = models.CharField(
        _('place_of_origin'),
        max_length=255
    )

    municipality_of_origin = models.CharField(
        _('municipality_of_origin'),
        max_length=255
    )

    sex = models.CharField(
        _('sex'),
        max_length=1,
        choices=SEX
    )

    age = models.PositiveSmallIntegerField(
        _('age'),
    )

    entrance_exam_score = models.DecimalField(
        _('entrance_exam_score'),
        max_digits=4,
        decimal_places=2
    )

    def __str__(self):
        return self.first_name + self.last_name
