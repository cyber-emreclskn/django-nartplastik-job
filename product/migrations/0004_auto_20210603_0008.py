# Generated by Django 3.1.7 on 2021-06-02 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_categoriesmodel_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriesmodel',
            options={'verbose_name': 'Kategoriler'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Ürünler'},
        ),
        migrations.AlterModelOptions(
            name='productimages',
            options={'verbose_name': 'Ürün Resimleri'},
        ),
    ]