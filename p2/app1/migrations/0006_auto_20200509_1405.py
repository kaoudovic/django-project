# Generated by Django 3.0.5 on 2020-05-09 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_staff_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='code',
            field=models.CharField(max_length=50, null=True),
        ),
    ]