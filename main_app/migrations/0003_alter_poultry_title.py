# Generated by Django 3.2.7 on 2021-09-02 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210902_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poultry',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
