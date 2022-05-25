from django.forms import models

from municipality.models import Municipality


class MunicipalityForm(models.ModelForm):
    class Meta:
        model = Municipality

        fields = '__all__'

        labels = {
            'municipality_name': 'Municipio',
            'state': 'Estado'
        }
