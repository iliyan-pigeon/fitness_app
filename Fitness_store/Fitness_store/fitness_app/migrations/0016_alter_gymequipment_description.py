# Generated by Django 4.2.4 on 2023-12-05 19:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0015_alter_supplements_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymequipment',
            name='description',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(300)]),
        ),
    ]
