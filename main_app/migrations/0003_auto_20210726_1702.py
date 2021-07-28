# Generated by Django 3.2.5 on 2021-07-26 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210726_1058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poultry',
            options={'ordering': ['-date_posted']},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='county',
            name='slug',
            field=models.SlugField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='poultry',
            name='slug',
            field=models.SlugField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='subcounty',
            name='slug',
            field=models.SlugField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='poultry',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poultries', to='main_app.category'),
        ),
        migrations.AlterField(
            model_name='poultry',
            name='county',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poultries', to='main_app.county'),
        ),
        migrations.AlterField(
            model_name='poultry',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='poultry',
            name='subcounty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poultries', to='main_app.subcounty'),
        ),
    ]