# Generated by Django 4.2.1 on 2023-05-12 12:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='presentation date'),
        ),
        migrations.AddField(
            model_name='deck',
            name='last_modified',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='last modified'),
        ),
    ]
