from django.contrib.sitemaps import Sitemap
from product.models import Product,CategoriesModel

class ProductSitemaps(Sitemap):

    def items(self):
        return Product.objects.all()