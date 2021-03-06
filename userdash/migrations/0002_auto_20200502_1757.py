# Generated by Django 2.2.11 on 2020-05-02 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estimate',
            name='created',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='order',
            name='starting_date',
            field=models.DateField(default='1995-5-10'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estimate',
            name='asking_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='estimate',
            name='estimated_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(),
        ),
    ]
