# Generated by Django 2.2.11 on 2020-04-10 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20200407_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='messagelog',
            name='phone',
            field=models.CharField(default='unknown', max_length=20),
        ),
    ]