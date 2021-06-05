from product.models import Product,CategoriesModel, ProductImages
from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from rangefilter.filter import DateTimeRangeFilter
from django.views.generic import ListView

class ProductListView(ListView):
    paginate_by = 2
    model = Product

class ProductImagesAd(admin.StackedInline):
    model = ProductImages
    extra = 1
    

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ('product_name',)}
    list_display = (
        'pk',
        'product_name',
        'product_categories',
        'created_at',
        'updated_at',
    )
    list_editable = (
        'product_name',
    )
    search_fields = (
        'product_name',
    )
    ordering = (
        'created_at',
        'updated_at',
    )
    list_filter = (
        ('product_categories',RelatedDropdownFilter),
        ('created_at', DateTimeRangeFilter),
    )
    inlines = [ProductImagesAd]

    date_hierarchy = 'updated_at'

    class Meta:

        model = Product


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ('categorie_name',)}
    list_display = [
        'pk',
        'categorie_name',
        'slug',
        'created_at',
        'updated_at',
    ]
    list_filter = ('categorie_name', )
    list_editable = list_filter


class ProductImagesAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'product',
    ]
    


admin.site.register(Product, ProductAdmin)
admin.site.register(CategoriesModel, CategoriesAdmin)
admin.site.register(ProductImages,ProductImagesAdmin)