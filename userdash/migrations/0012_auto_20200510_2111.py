# Generated by Django 2.2.11 on 2020-05-10 21:11

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('userdash', '0011_auto_20200508_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimate',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]