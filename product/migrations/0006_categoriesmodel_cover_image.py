# Generated by Django 3.1.7 on 2021-06-03 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210603_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriesmodel',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='category_main_image', verbose_name='Kategori Resmi'),
        ),
    ]