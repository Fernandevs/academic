from django.forms import models

from locality.models import Locality


class LocalityForm(models.ModelForm):
    class Meta:
        model = Locality

        fields = '__all__'

        labels = {
            'locality_name': 'Localidad',
            'municipality': 'Municipio'
        }
