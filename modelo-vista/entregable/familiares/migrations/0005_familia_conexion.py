# Generated by Django 4.1.3 on 2022-11-06 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares', '0004_familia_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='familia',
            name='Conexion',
            field=models.TextField(blank=True),
        ),
    ]
