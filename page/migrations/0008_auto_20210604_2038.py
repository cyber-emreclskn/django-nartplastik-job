# Generated by Django 3.1.7 on 2021-06-04 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_auto_20210604_2029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='whatjob',
            options={'verbose_name': 'Neler Yapıyoruz Bilgileri', 'verbose_name_plural': 'Neler Yapıyoruz'},
        ),
        migrations.AlterModelOptions(
            name='whyus',
            options={'verbose_name': 'Neden Biz Bilgileri', 'verbose_name_plural': 'Neden Biz'},
        ),
        migrations.AddField(
            model_name='whatjob',
            name='icon_code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='icon_code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
