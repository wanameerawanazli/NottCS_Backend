# Generated by Django 2.0.2 on 2018-02-09 19:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('azureAD_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='azureaduser',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='azureaduser',
            name='is_authenticated',
            field=models.BooleanField(default=True),
        ),
    ]
