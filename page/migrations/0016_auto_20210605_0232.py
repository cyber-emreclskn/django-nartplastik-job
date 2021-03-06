# Generated by Django 3.1.7 on 2021-06-04 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0015_auto_20210605_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='smtp_host',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='smtp_mail_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='smtp_mail_password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='smtp_mail_server',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
