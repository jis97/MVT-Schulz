# Generated by Django 4.0.3 on 2022-03-30 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2022, 3, 30, 11, 44, 9, 262753)),
        ),
    ]
