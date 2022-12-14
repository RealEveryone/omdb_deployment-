# Generated by Django 4.1.3 on 2022-12-08 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, null=True, to='user.actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, null=True, to='movie.moviegenres'),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.moviedirector'),
        ),
    ]