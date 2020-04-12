# Generated by Django 2.2.11 on 2020-04-07 12:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagelog',
            name='message',
        ),
        migrations.RemoveField(
            model_name='messagelog',
            name='title',
        ),
        migrations.AddField(
            model_name='messagelog',
            name='log',
            field=models.TextField(default=datetime.datetime(2020, 4, 7, 12, 21, 32, 102935, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='messagetemplate',
            name='message',
            field=models.TextField(),
        ),
    ]