from django.forms import models

from careers.models import Career


class CareerCreateForm(models.ModelForm):
    class Meta:
        model = Career

        fields = [
            'career',
        ]

        labels = {
            'career': 'Carrera',
        }


class CareerUpdateForm(models.ModelForm):
    class Meta:
        model = Career

        fields = [
            'career',
            'is_active'
        ]

        labels = {
            'career': 'Carrera',
            'is_active': 'Está activo'
        }
