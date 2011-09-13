from cms.models import CMSPlugin
from django.db import models
from shop.models.productmodel import Product
from django.utils.translation import ugettext_lazy as _

class TopProducts(CMSPlugin):
    products = models.ManyToManyField(Product, verbose_name=_('products'), blank=True, null=True,
        help_text=_('Shows the selected products.'))
    