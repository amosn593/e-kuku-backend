# Generated by Django 3.2.5 on 2021-07-28 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_rename_name_poultry_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='poultry',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='poultry_images/'),
        ),
    ]