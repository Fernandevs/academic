from django.forms import models

from students.models import Student


class StudentForm(models.ModelForm):
    class Meta:
        model = Student

        fields = '__all__'

        labels = {
            'first_name': 'Nombre(s)',
            'last_name': 'Apellidos',
            'career': 'Carrera',
            'plan': 'Plan de estudios',
            'period': 'Periodo',
            'year': 'Año',
            'record_number': 'Número de ficha',
            'control_number': 'Número de control',
            'school_of_origin': 'Escuela de procedencia',
            'average': 'Promedio',
            'place_of_origin': 'Localidad de origen',
            'municipality_of_origin': 'Municipio de origen',
            'sex': 'Sexo',
            'age': 'Edad',
            'entrance_exam_score': 'Calificación del examen de ingreso',
        }
