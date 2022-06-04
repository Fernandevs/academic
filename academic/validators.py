import decimal
from decimal import Decimal

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def name_validator(value: str):
    values = value.split()

    for val in values:
        if not val.isalpha():
            raise ValidationError(
                _('%(value)s no es alfabético'),
                params={'value': value},
            )


def number_validator(value: str):
    if not value.isdigit():
        raise ValidationError(
            _('%(value)s no es numérico'),
            params={'value': value},
        )


def day_validator(value: str):
    day = int(value)

    if day < 1 or day > 31:
        raise ValidationError(
            _('%(value)s no está dentro del rango esperado'),
            params={'value': value},
        )


def month_validator(value: str):
    month = int(value)

    if month < 1 or month > 12:
        raise ValidationError(
            _('%(value)s no está dentro del rango esperado'),
            params={'value': value},
        )


def year_validator(value: str):
    year = int(value)

    if year < 1900 or year > 2099:
        raise ValidationError(
            _('%(value)s no está dentro del rango esperado'),
            params={'value': value},
        )


def high_school_average_validator(value: Decimal):
    average = Decimal(value)

    if average < 6.0 or average > 10.0:
        raise ValidationError(
            _('%(value)s no está dentro del rango esperado'),
            params={'value': value},
        )
