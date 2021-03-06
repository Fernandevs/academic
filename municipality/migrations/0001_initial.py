# Generated by Django 4.0.1 on 2022-06-07 18:30

import academic.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('state', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipality_id', models.CharField(default='053', max_length=3, validators=[academic.validators.number_validator], verbose_name='id municipality')),
                ('municipality_name', models.CharField(max_length=255, validators=[academic.validators.name_validator], verbose_name='municipality')),
                ('state', models.ForeignKey(default='16', on_delete=django.db.models.deletion.CASCADE, to='state.state')),
            ],
        ),
    ]
