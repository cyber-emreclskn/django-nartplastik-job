# Generated by Django 3.1.7 on 2021-06-04 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0012_auto_20210605_0047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitesettings',
            old_name='facebook_account',
            new_name='facebook_hesabi',
        ),
        migrations.RenameField(
            model_name='sitesettings',
            old_name='corporate_mail_adress',
            new_name='firma_mail_adres',
        ),
        migrations.RenameField(
            model_name='sitesettings',
            old_name='corporate_phone_number',
            new_name='firma_telefonu',
        ),
        migrations.RenameField(
            model_name='sitesettings',
            old_name='instagram_account',
            new_name='instagram_hesabi',
        ),
        migrations.RenameField(
            model_name='sitesettings',
            old_name='personal_phone_number',
            new_name='kisisel_telefon_numarasi',
        ),
        migrations.RenameField(
            model_name='sitesettings',
            old_name='linkedin_account',
            new_name='linkedin_hesabi',
        ),
        migrations.RenameField(
            model_name='sitesettings',
            old_name='mail_adress',
            new_name='mail_adresi',
        ),
        migrations.RenameField(
            model_name='sitesettings',
            old_name='site_desc',
            new_name='site_aciklama',
        ),
        migrations.RenameField(
            model_name='sitesettings',
            old_name='twitter_account',
            new_name='twitter_hesabi',
        ),
    ]
