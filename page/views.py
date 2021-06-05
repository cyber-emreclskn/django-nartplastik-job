from django.shortcuts import render, redirect, reverse
from .models import Carousel, ContactModel, Page, SiteSettings, WhatJob, WhoUs, WhyUs
from product.models import Product, CategoriesModel, ProductImages
from django.core.paginator import EmptyPage, Paginator
from .mailbackend import send_mail

# Create your views here.


def index(request):
    context = dict()
    site_settings = SiteSettings.objects.get(site_ismi = 'Nart Plastik')
    context['site_settings'] = site_settings
    keyword = request.GET.get('keyword')
    categories = CategoriesModel.objects.all()
    products = Product.objects.all()[:5]
    pages = Page.objects.all()
    productsImages = ProductImages.objects.all()

    footer_product = Product.objects.all()[:5]
    footer_catregories = CategoriesModel.objects.all()[:5]
    context['footer_p'] = footer_product
    context['footer_c'] = footer_catregories
    context['keyword'] = keyword
    who_us = WhoUs.objects.get(
        title='Biz Kimiz'
    )

    paginator = Paginator(products, 6)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    why_us = WhyUs.objects.all()
    what_job = WhatJob.objects.all()
    context['why_us'] = why_us
    context['what_job'] = what_job
    context['who_us'] = who_us

    context['product_images'] = productsImages
    context['products'] = products
    context['categories'] = categories
    context['pages'] = pages
    if keyword:
        products_c = Product.objects.filter(product_name__contains=keyword)
        context['products'] = products_c
        paginator = Paginator(products_c, 6)  # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return render(request, "products.html", context)

    return render(request, "index.html", context)


def contact(request):
    context = dict()
    mail_to = SiteSettings.objects.get(site_ismi = 'Nart Plastik')
    context['site_settings'] = mail_to
    pages = Page.objects.all()
    categories = CategoriesModel.objects.all()
    context['pages'] = pages
    context['categories'] = categories
    if request.method == "POST":
        full_name = request.POST.get('full-name')
        from_mail = request.POST.get('from-mail')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        context = {
            'full-name': full_name,
            'from-mail': from_mail,
            'subject': subject,
            'message': message,
        }

        contact_model = ContactModel(
            full_name=context['full-name'],
            from_mail=context['from-mail'],
            subject=context['subject'],
            message=context['message'],
        )

        contact_model.save()

        message = """
            New Message : {}

            From : {}
        """.format(context['message'], context['from-mail'])
        
        send_mail(context['subject'],mail_to.smtp_mail_name, message)

    footer_product = Product.objects.all()[:5]
    footer_catregories = CategoriesModel.objects.all()[:5]
    context['footer_p'] = footer_product
    context['footer_c'] = footer_catregories

    return render(request, "contact.html", context)


def detail(request, slug_product):
    context = dict()
    site_settings = SiteSettings.objects.get(site_ismi = 'Nart Plastik')
    context['site_settings'] = site_settings
    pages = Page.objects.all()
    categories = CategoriesModel.objects.all()
    products = Product.objects.all()

    product_s = Product.objects.get(
        slug=slug_product
    )
    category_slug = CategoriesModel.objects.get(
        categorie_name=product_s.product_categories
    )

    product_images = ProductImages(
        product=product_s
    )

    image_list = list()
    for image in product_images.image_list(product_s):
        if image.cover_image:
            image_list.append(image.cover_image.url)
            print(image.cover_image.url)
        else:
            image_list = list()

    context['category_slug'] = category_slug
    context['products'] = products
    context['pages'] = pages
    context['categories'] = categories
    context['product'] = product_s
    context['product_images_urls'] = image_list

    footer_product = Product.objects.all()[:5]
    footer_catregories = CategoriesModel.objects.all()[:5]
    context['footer_p'] = footer_product
    context['footer_c'] = footer_catregories

    return render(request, "details.html", context)


def filter_by_category(request, slug_new):

    context = dict()
    site_settings = SiteSettings.objects.get(site_ismi = 'Nart Plastik')
    context['site_settings'] = site_settings
    pages = Page.objects.all()
    categories = CategoriesModel.objects.all()
    products_s = Product.objects.filter(
        product_categories=CategoriesModel.objects.get(slug=slug_new)
    )
    productsImages = ProductImages.objects.all()

    paginator = Paginator(products_s, 6)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['pages'] = pages
    context['product_images'] = productsImages
    context['products'] = products_s
    context['page_obj'] = page_obj
    context['categories'] = categories
    context['category_slug'] = slug_new

    footer_product = Product.objects.all()[:5]
    footer_catregories = CategoriesModel.objects.all()[:5]
    context['footer_p'] = footer_product
    context['footer_c'] = footer_catregories

    return render(request, "products.html", context)


def products(request):
    context = dict()
    site_settings = SiteSettings.objects.get(site_ismi = 'Nart Plastik')
    context['site_settings'] = site_settings
    categories = CategoriesModel.objects.all()
    products = Product.objects.all()
    pages = Page.objects.all()
    productsImages = ProductImages.objects.all()

    paginator = Paginator(products, 6)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['product_images'] = productsImages
    context['pages'] = pages
    context['products'] = products
    context['categories'] = categories
    context['page_obj'] = page_obj

    footer_product = Product.objects.all()[:5]
    footer_catregories = CategoriesModel.objects.all()[:5]
    context['footer_p'] = footer_product
    context['footer_c'] = footer_catregories

    return render(request, "products.html", context)


def corporate_filter(request, slug_new):
    context = dict()
    site_settings = SiteSettings.objects.get(site_ismi = 'Nart Plastik')
    context['site_settings'] = site_settings
    products = Product.objects.all()[:5]
    context['products'] = products
    pages = Page.objects.all()
    filter_page = Page.objects.filter(slug=slug_new)
    carosel_images = Carousel.objects.filter(page=filter_page)
    categories = CategoriesModel.objects.all()
    context['categories'] = categories
    context['filter_page'] = filter_page

    context['pages'] = pages

    context['active_slug'] = slug_new

    footer_product = Product.objects.all()[:5]
    footer_catregories = CategoriesModel.objects.all()[:5]
    context['footer_p'] = footer_product
    context['footer_c'] = footer_catregories

    return render(request, "kurumsal.html", context)
