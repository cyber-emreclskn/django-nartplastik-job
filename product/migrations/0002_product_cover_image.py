# Generated by Django 3.1.7 on 2021-06-01 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_main_image'),
        ),
    ]
