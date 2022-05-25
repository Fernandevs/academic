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
