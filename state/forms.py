from django.forms import models

from state.models import State


class StateForm(models.ModelForm):
    class Meta:
        model = State

        fields = '__all__'

        labels = {
            'state_name': 'Estado'
        }
