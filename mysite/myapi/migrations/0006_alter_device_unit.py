# Generated by Django 3.2.2 on 2021-05-15 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_auto_20210515_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='unit',
            field=models.CharField(default='', max_length=100),
        ),
    ]
