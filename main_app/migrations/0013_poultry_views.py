# Generated by Django 3.2.5 on 2021-07-30 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_alter_poultry_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='poultry',
            name='views',
            field=models.IntegerField(default=1),
        ),
    ]
