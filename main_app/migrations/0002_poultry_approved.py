# Generated by Django 3.2.5 on 2021-07-31 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poultry',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]