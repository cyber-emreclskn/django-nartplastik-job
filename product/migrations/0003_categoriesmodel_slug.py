# Generated by Django 3.1.7 on 2021-06-01 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriesmodel',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
    ]
