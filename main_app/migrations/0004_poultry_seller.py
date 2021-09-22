# Generated by Django 3.2.7 on 2021-09-11 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_alter_poultry_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='poultry',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sells', to=settings.AUTH_USER_MODEL),
        ),
    ]