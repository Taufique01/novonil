# Generated by Django 2.1.7 on 2020-03-13 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_auto_20200309_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField(default=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Additional',
            new_name='Optional',
        ),
    ]
