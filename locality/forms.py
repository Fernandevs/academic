from django.forms import models, forms

from locality.models import Locality


class LocalityForm(models.ModelForm):
    class Meta:
        model = Locality

        fields = '__all__'

        labels = {
            'locality_id': 'ID',
            'locality_name': 'Localidad',
            'municipality': 'Municipio',
            'state': 'Estado'
        }
