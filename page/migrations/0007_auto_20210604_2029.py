# Generated by Django 3.1.7 on 2021-06-04 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_auto_20210604_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatjob',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='whyus',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
