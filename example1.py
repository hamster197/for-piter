from django.core import serializers
from django.db.models import Sum, Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db import models

class Product(models.Model):
    categories = models.ManyToManyField(Category,
                                        related_name='products',
                                        blank=True, verbose_name=u"категории")
    related_products = models.ManyToManyField('Product',
                                              blank=True,
                                              verbose_name="связанные продукты")

    sku = models.CharField(u'артикул', max_length=128, validators=[validators.check_bad_symbols], unique=True)

    price = models.DecimalField(u'цена', max_digits=12, decimal_places=4)

    slug = models.SlugField(u'slug', max_length=80, db_index=True, unique=True)

    name = models.CharField(u'название', max_length=128)
    title = models.CharField(u'заголовок страницы (<title>)', max_length=256, blank=True)
    description = models.TextField(u'описание', blank=True)



def test(request, template_name="shop/livesearch_results.html"):
    q = request.GET.get("q", "")
    p = Product.objects.filter(Q(sku__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))
    qs = serializers.serialize('json', p)
    return HttpResponse(qs, content_type='application/json')
