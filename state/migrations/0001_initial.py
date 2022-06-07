# Generated by Django 4.0.1 on 2022-06-07 18:30

import academic.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.CharField(default='16', error_messages={'unique': 'Ya existe un estado con ese identificador.'}, max_length=2, primary_key=True, serialize=False, unique=True, validators=[academic.validators.number_validator], verbose_name='id state')),
                ('state_name', models.CharField(max_length=255, unique=True, validators=[academic.validators.name_validator], verbose_name='state')),
            ],
        ),
    ]