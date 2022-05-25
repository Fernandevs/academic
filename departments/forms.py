from django.forms import models

from departments.models import Department


class DepartmentForm(models.ModelForm):
    class Meta:
        model = Department

        fields = '__all__'

        labels = {
            'department_name': 'Nombre del departamento',
            'department_owner': 'Encargado del departamento',
        }
