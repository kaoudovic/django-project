# Generated by Django 3.0.5 on 2020-05-09 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_staff_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='code',
            field=models.CharField(default='dodo', max_length=50),
            preserve_default=False,
        ),
    ]
