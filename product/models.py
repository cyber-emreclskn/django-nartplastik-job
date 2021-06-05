from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class CategoriesModel(models.Model):

    categorie_name = models.CharField(
        max_length=100,
        verbose_name="Kategori İsmi",
    )
    slug = models.SlugField(
        max_length=200,
        default="",
    )
    cover_image = models.ImageField(
        verbose_name='Kategori Resmi',
        upload_to = 'category_main_image',
        null = True,
        blank = True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.categorie_name

    def count(self):
        return str(Product.objects.filter(product_categories = self.pk).count())

    class Meta:
        verbose_name = 'Kategoriler'
        verbose_name_plural = 'Kategoriler'
class Product(models.Model):

    product_name = models.CharField(
        max_length=250,
        verbose_name="Ürün İsmi"
        )
    product_desc = models.TextField()
    product_categories = models.ForeignKey(
        CategoriesModel,
        on_delete=models.CASCADE,
        verbose_name="Ürün Kategorisi",
        related_name="Kategori",
        null=True,
        blank=True,
        )
    slug = models.SlugField(
        max_length=200,
        default="",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(
        upload_to = 'product_main_image',
        null = True,
        blank = True,
    )
    
    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı','i'))
        unique_slug = slug
        counter = 1
        while Product.objects.filter(slug = unique_slug).exists():
            unique_slug = '{}-{}'.format(slug,counter)
        
        return unique_slug

    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse('product', args=[str(self.slug)])

    def count(self):
        return str(Product.objects.filter.all().count())
    
    

    class Meta:
        verbose_name = 'Ürünler'
        verbose_name_plural = 'Ürünler'

class ProductImages(models.Model):

    image_name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Ürün Resmi",
        related_name="Resim"
    )
    cover_image = models.ImageField(
        upload_to='product',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.product.product_name

    def image_list(self,product):
        image_list = ProductImages.objects.filter(
            product = product
        )
        return image_list

    class Meta:
        verbose_name = 'Ürün Resimleri'
        verbose_name_plural = 'Ürün Resimleri'

