# Generated by Django 4.2.1 on 2023-05-22 12:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mat_fotbal', '0005_remove_klub_turnaje_delete_turnaments_klub_turnaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='liga',
            name='zalozeni',
            field=models.IntegerField(default='1900', help_text='Zadejte rok založení ligy', validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2023)], verbose_name='Rok zalozeni'),
        ),
    ]
