# Generated by Django 4.2.4 on 2023-12-05 15:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0014_alter_order_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplements',
            name='description',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(300)]),
        ),
    ]
