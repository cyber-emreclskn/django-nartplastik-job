# Generated by Django 3.1.7 on 2021-06-06 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0018_auto_20210606_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='firma_harita_link',
            field=models.TextField(blank=True, null=True, verbose_name='Firma Harita Link(Burasını Gerekmedikçe Değiştirmeyin)'),
        ),
    ]