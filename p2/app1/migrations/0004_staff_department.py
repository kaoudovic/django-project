# Generated by Django 3.0.5 on 2020-05-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20200509_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='department',
            field=models.CharField(max_length=50, null=True),
        ),
    ]