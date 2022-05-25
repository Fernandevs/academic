from django.forms import models

from egress.models import Egress


class EgressForm(models.ModelForm):
    class Meta:
        model = Egress

        fields = '__all__'

        labels = {
            'id_number': 'Número de control',
            'student_name': 'Nombre',
            'paternal_surname': 'Apellido paterno',
            'maternal_surname': 'Apellido materno',
            'career': 'Carrera',
            'option': 'Opción de titulación',
            'egress_period': 'Periodo de egreso',
            'egress_year': 'Año de egreso'
        }


"""
    'career': 'Carrera',
    'plan': 'Plan de estudios',
    'egress_period': 'Periodo de egreso',
    'egress_year': 'Año de egreso',
    'graduation_period': 'Periodo de graduación',
    'graduation_year': 'Año de graduación',
    'id_number': 'Número de control',
    'option': 'Opción de egreso',
    'degree_date': 'Fecha de titulación',
    'egress_date': 'Fecha de egreso'
"""
