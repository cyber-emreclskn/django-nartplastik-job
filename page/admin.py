from django.contrib import admin
from .models import Carousel, ContactModel, Page, SiteSettings, WhatJob, WhyUs, WhoUs
from django.utils import timezone
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from rangefilter.filter import DateTimeRangeFilter
from nartplastik import settings


class Images(admin.StackedInline):
    model = Carousel
    extra = 1
    classes = ('collapse',)

class CarouselAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'page',
        'title',
        'cover_image',
    ]
    search_fields = ['title']


class PageAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {"slug" : ('title',)}
    list_display = (
        'pk',
        'title',
        'slug',
        'status',
        'created_at',
        'updated_at',
        'kac_gun_once'
    )
    list_filter = (
       'status',
       ('created_at',DateTimeRangeFilter),
    )
    '''
    list_editable = (
        'title',
        'status',
    )
    '''
    '''
    fields = (
        'title',
        'slug',
        'content',
        'cover_image',
        'status',
    )
    '''

    fieldsets = (
        (None,{
            'fields' : (('title','slug'),'content','status'),
            'description' : 'Sayfa İçin Gerekli Ayarlar',
        }),
        ('Opsiyonel Ayarlar',{
            'fields': ('cover_image',),
            'description' : 'Opsiyonel Ayarlar İçin Bu Kümeyi Kullanabilirsiniz',
            'classes' : ('collapse',),
        })
    )

    def kac_gun_once(self,page):
        fark = timezone.now() - page.created_at
        return fark.days

    inlines = [Images]


    



class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'full_name',
        'from_mail',
        'subject',
        'created_at'
    ]
    search_fields = [
        'from_mail',
        'subject',
    ]
    readonly_fields = [
        
        'full_name',
        'from_mail',
        'subject',
        'created_at',
        'message'
    ]

class WhyUsAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title'
    ]
class WhatJobAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title'
    ]

class WhoUsAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title'
    ]

class SiteSettingsAdmin(admin.ModelAdmin):

    fieldsets = (
        (None,{
            'fields' : (
                'site_ismi',
                'site_keywords',
                'site_aciklama',
                'smtp_port',
                'smtp_mail_server',
                'smtp_mail_name',
                'smtp_mail_password',
                'google_analytics',
                'google_adsense',
                'google_search',
                'firma_harita_kodu',
                'firma_telefonu',
                'firma_mail_adres',
                'firma_harita_link',
                
            ),
            'description' : 'Site İçin Gerekli Ayarlar',
        }),
        ('Opsiyonel Ayarlar',{
            'fields': (
                'firma_kisa_adres',
                'instagram_hesabi',
                'twitter_hesabi',
                'facebook_hesabi',
                'linkedin_hesabi',
                'kisisel_telefon_numarasi',
                'mail_adresi',
            ),
            'description' : 'Opsiyonel Ayarlar İçin Bu Kümeyi Kullanabilirsiniz',
            'classes' : ('collapse',),
        })
    )

admin.site.register(SiteSettings ,SiteSettingsAdmin)
admin.site.register(WhoUs, WhoUsAdmin)
admin.site.register(WhyUs, WhyUsAdmin)
admin.site.register(WhatJob, WhatJobAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(ContactModel,ContactAdmin)
