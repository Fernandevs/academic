from django.forms import models

from school.models import School


class SchoolForm(models.ModelForm):
    class Meta:
        model = School

        fields = '__all__'

        labels = {
            'school_name': 'Escuela',
            'catchword': 'Lema',
            'logo': 'Logo',
            'level': 'Nivel',
            'control': 'Control',
            'clue': 'Clave',
            'sustenance': 'Sostenimiento',
            'location': 'Dirección',
            'municipality': 'Municipio',
            'student_population': 'Número de estudiantes',
            'teaching_population': 'Número de maestros',
        }
