# Generated by Django 5.0.7 on 2024-08-26 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_cart_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='proceed_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Last_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Country', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Town', models.CharField(blank=True, max_length=100, null=True)),
                ('State', models.CharField(blank=True, max_length=100, null=True)),
                ('Pincode', models.IntegerField(blank=True, null=True)),
                ('Phone', models.IntegerField(blank=True, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
