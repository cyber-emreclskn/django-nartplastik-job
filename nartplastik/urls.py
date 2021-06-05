"""nartplastik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, sitemaps
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from page.views import index
from django.contrib.sitemaps.views import sitemap
from page.sitemaps import ProductSitemaps

from product.views import products_s

sitemaps = {
    'products':ProductSitemaps,
}

urlpatterns = [
    path('',index,name="index"),
    path('page/',include(('page.urls', 'page'), namespace='page')),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap'),
    path('products/<slug:slug>',products_s,name='product')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

admin.site.site_title = 'NartPlastik Admin'

admin.site.site_header = 'NartPlastik Admin Sayfası'

admin.site.index_title = 'NartPlastik Yönetim Sayfasına Hoşgeldiniz'