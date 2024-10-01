# Generated by Django 5.0.7 on 2024-08-04 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_signin_db'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signin_db',
            old_name='Username',
            new_name='Confirm_Password',
        ),
        migrations.AddField(
            model_name='signin_db',
            name='Name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
