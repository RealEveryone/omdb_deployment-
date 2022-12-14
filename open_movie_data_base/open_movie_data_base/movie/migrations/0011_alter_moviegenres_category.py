# Generated by Django 4.1.3 on 2022-12-14 12:15

from django.db import migrations, models
import open_movie_data_base.utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_alter_movie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviegenres',
            name='category',
            field=models.CharField(blank=True, max_length=50, unique=True, validators=[open_movie_data_base.utils.validators.CharValidator('^[A-Za-z\\w-]+\\Z', 'Use only latin letters, spaces and dashes')]),
        ),
    ]
