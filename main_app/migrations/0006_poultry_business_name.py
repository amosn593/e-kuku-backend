# Generated by Django 3.2.7 on 2021-10-01 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210922_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='poultry',
            name='business_name',
            field=models.CharField(default='supplier', max_length=15),
            preserve_default=False,
        ),
    ]
