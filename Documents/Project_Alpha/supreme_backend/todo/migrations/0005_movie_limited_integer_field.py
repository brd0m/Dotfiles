# Generated by Django 4.1 on 2022-08-08 02:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_movie_title_short'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='limited_integer_field',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]