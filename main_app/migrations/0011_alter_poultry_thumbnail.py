# Generated by Django 3.2.5 on 2021-07-28 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_poultry_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poultry',
            name='thumbnail',
            field=models.ImageField(default='poultry_images/default.jpg', upload_to='poultry_images/'),
        ),
    ]