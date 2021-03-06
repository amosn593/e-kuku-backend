# Generated by Django 3.2.7 on 2021-09-10 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_useraccount_date_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='name',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='user_name',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
