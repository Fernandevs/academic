from django.forms import models

from students.models import Student


class StudentForm(models.ModelForm):
    class Meta:
        model = Student

        fields = '__all__'
