# Generated by Django 4.0.3 on 2022-03-29 05:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2022, 3, 29, 2, 45, 30, 491874)),
        ),
    ]