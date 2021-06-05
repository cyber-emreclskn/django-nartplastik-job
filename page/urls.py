from django.urls import path

from . import views

urlpatterns = [
    path('iletisim',views.contact,name="contact"),
    path('urunler',views.products,name="products"),
    path('kategori/<slug:slug_new>',views.filter_by_category,name = "filter_category"),
    path('kurumsal/<slug:slug_new>',views.corporate_filter,name="corporate"),
    path('urun-detay/<slug:slug_product>',views.detail,name="details"),
]