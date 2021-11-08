# Generated by Django 3.2.7 on 2021-10-28 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_poultry_business_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='poultry',
            name='sponsored',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='poultry',
            name='business_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='poultry',
            name='description',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='poultry',
            name='price',
            field=models.CharField(default='Negotiable', max_length=50),
        ),
    ]