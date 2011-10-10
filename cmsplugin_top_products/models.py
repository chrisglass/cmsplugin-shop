from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from shop.models.productmodel import Product

class TopProducts(CMSPlugin):
    products = models.ManyToManyField(Product, verbose_name=_('products'), blank=True, null=True,
        help_text=_('Shows the selected products.'))
    