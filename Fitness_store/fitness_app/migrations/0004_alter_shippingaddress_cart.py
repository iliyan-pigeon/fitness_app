# Generated by Django 4.2.4 on 2023-11-08 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0003_shippingaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='cart',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]