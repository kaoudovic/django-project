# Generated by Django 3.0.5 on 2020-05-07 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='birthday',
        ),
    ]