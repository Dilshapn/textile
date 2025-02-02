# Generated by Django 5.0.7 on 2024-07-22 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Product_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Description', models.TextField(blank=True, max_length=50, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Brand', models.CharField(blank=True, max_length=50, null=True)),
                ('Product_img1', models.ImageField(blank=True, null=True, upload_to='product image')),
                ('Product_img2', models.ImageField(blank=True, null=True, upload_to='product image')),
                ('Product_img3', models.ImageField(blank=True, null=True, upload_to='product image')),
            ],
        ),
    ]
