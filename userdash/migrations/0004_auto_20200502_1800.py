# Generated by Django 2.2.11 on 2020-05-02 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdash', '0003_auto_20200502_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='starting_date',
        ),
    ]
