# Generated by Django 3.2.2 on 2021-05-12 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_rename_hero_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.CharField(max_length=100),
        ),
    ]
