# Generated by Django 5.1.4 on 2025-01-27 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connectgmail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gmail_users',
            name='Is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='gmail_users',
            name='Is_superviser',
            field=models.BooleanField(default=False),
        ),
    ]