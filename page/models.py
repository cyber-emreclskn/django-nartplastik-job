from django.db import models
from django.utils.text import Truncator, slugify
from ckeditor.fields import RichTextField
from django.conf import settings

DEFAULT_STATUS = "draft"

STATUS = [
    ('draft','Taslak'),
    ('published','Yayinlandi'),
    ('deleted','Silindi'),
]

class Page(models.Model):
    
    title = models.CharField(max_length=200)
    content = RichTextField()
    cover_image = models.ImageField(
        upload_to='page',
        null=True,
        blank=True,
        )
    slug = models.SlugField(
        max_length=200,
        default="",
    )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Sayfalar'
        verbose_name_plural = 'Sayfalar'
    def __str__(self):
        return self.slug

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı','i'))
        unique_slug = slug
        counter = 1
        while Page.objects.filter(slug = unique_slug).exists():
            unique_slug = '{}-{}'.format(slug,counter)
        
        return unique_slug
    
    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Page, self).save(*args,**kwargs)


class Carousel(models.Model):

    page = models.ForeignKey(
        Page,
        on_delete=models.CASCADE,
        verbose_name="Sayfa Resmi",
        related_name="Resim"
    )
    title = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        )
    #status = models.CharField(
    #    default=DEFAULT_STATUS,
    #    choices=STATUS,
    #    max_length=10,
    #)
    cover_image = models.ImageField(
        upload_to='carousel',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    upadated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Ayrı Resimler'
        verbose_name_plural = 'Resimler'

class ContactModel(models.Model):

    full_name = models.CharField(
        max_length=200,
        verbose_name="Gönderen İsim",
    )
    from_mail = models.EmailField(
        max_length=200,
        verbose_name="Gönderen Mail",
    )
    subject = models.CharField(
        max_length=150,
        verbose_name="Mesaj Konusu",
    )
    message = models.TextField(
        verbose_name="Mesaj",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişimler'


class WhyUs(models.Model):
    title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    icon_code = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    content = models.TextField()
    class Meta:
        verbose_name = 'Neden Biz Bilgileri'
        verbose_name_plural = 'Neden Biz'

class WhatJob(models.Model):
    title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    icon_code = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    content = models.TextField()
    class Meta:
        verbose_name = 'Neler Yapıyoruz Bilgileri'
        verbose_name_plural = 'Neler Yapıyoruz'

class WhoUs(models.Model):
    title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    content = models.TextField(
        null=True,
        blank=True,
    )
    class Meta:
        verbose_name = 'Biz Kimiz Bilgileri'
        verbose_name_plural = 'Biz Kimiz'

class SiteSettings(models.Model):
    
    site_ismi = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Site İsmi(Nart Plastik olmalı)'
    )
    firma_mail_adres = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Firmanın Mail Adresi'
    )
    firma_telefonu = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Firma Telefon Numarası'
    )
    firma_kisa_adres = models.CharField(
        max_length=450,
        null=True,
        blank=True,
        verbose_name='Firma Kısa Adresi'
    )
    firma_harita_kodu = models.TextField(
        null=True,
        blank=True,
        verbose_name='Harita Kodu(Google Maps Kodu)'
    )
    site_aciklama = models.TextField(
        null=True,
        blank=True,
        verbose_name='Site Açıklaması(Site)(Google Kısmı)'
    )
    site_keywords = models.TextField(
        null=True,
        blank=True,
        verbose_name='Site Anahtar Kelimeleri(Keywords)'
    )
    smtp_mail_server = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    smtp_mail_name = models.CharField(
        
        max_length=200,
        null=True,
        blank=True,
    )
    smtp_port = models.IntegerField(
        null=True,
        blank=True,
    )
    smtp_mail_password = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    google_analytics = models.TextField(
        null=True,
        blank=True,
        verbose_name='Google Anaylytics Kodu(Burayı Gerekmedikçe Değiştirmeyin)'
    )
    google_adsense = models.TextField(
        null=True,
        blank=True,
        verbose_name='Google Adsense Kodu(Burayı Gerekmedikçe Değiştirmeyin)'
    )
    google_search = models.TextField(
        null=True,
        blank=True,
        verbose_name='Google Search Kodu(Burayı Gerekmedikçe Değiştirmeyin)'
    )
    instagram_hesabi = models.CharField(
        max_length=200,
        verbose_name='Instagram Adresi',
        null=True,
        blank=True,
    )
    twitter_hesabi = models.CharField(
        max_length=200,
        verbose_name='Twitter Adresi',
        null=True,
        blank=True,
    )
    facebook_hesabi = models.CharField(
        max_length=200,
        verbose_name='Facebook Adresi',
        null=True,
        blank=True,
    )
    linkedin_hesabi = models.CharField(
        max_length=200,
        verbose_name='Linkedin Adresi',
        null=True,
        blank=True,
    )
    kisisel_telefon_numarasi = models.CharField(
       max_length=200,
       verbose_name='Telefon Numarası',
       null=True,
       blank=True, 
    )
    mail_adresi = models.CharField(
       max_length=200,
       verbose_name='Mail Adresi',
       null=True,
       blank=True, 
    )
    firma_harita_link = models.TextField(
        null=True,
        blank=True,
        verbose_name='Firma Harita Link(Burasını Gerekmedikçe Değiştirmeyin)'
    )

    class Meta:
        verbose_name = 'Site Ayarları'
        verbose_name_plural = 'Ayarlar'