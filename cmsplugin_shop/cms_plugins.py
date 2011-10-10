from django.db.models import Count
from django.template.defaultfilters import title
from django.utils.translation import ugettext_lazy as _


from cms.models.pluginmodel import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from shop.util.cart import get_or_create_cart
from shop.models.productmodel import Product
from shop.models.ordermodel import OrderItem

from models import TopProducts

class CartCMSPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("django SHOP Cart")
    render_template = "cmsplugin_shop/cart.html"

    def render(self, context, instance, placeholder):
        request = context['request']
        cart = get_or_create_cart(request)
        cart_items = cart.items
        
        context.update({'cart':cart})
        context.update({'cart_items':cart_items})

        return context

    

plugin_pool.register_plugin(CartCMSPlugin)

class TopProductsPlugin(CMSPluginBase):
    model = TopProducts
    admin_preview = False
    name = title(_('top products plugin'))
    placeholders = ('feature_home',)
    render_template = "top_products/plugins/top_products.html"
    
    def render(self, context, instance, placeholder):
        """This is the main rendering function. We "simply" query the database
        to get the top N products (as defined in the plugin instance), and pass
        them to the context"""

        top_products_data = OrderItem.objects.values(
        'product_reference').annotate(
        product_count=Count('product_reference')).order_by('product_count')[:instance.number_of_products]
        
        # The top_products_data result should be in the form:
        # [{'product_reference': '<product_id>', 'product_count': <count>}, ...]
        
        top_products_list = []
        for values in top_products_data:
            prod = Product.objects.get(pk=values.get('product_reference'))
            count = values.get('product_count')
            top_products_list.append({'object': prod, 'count' : count})
        
        # TODO: Cache top_products_list, invalidate on new order (or just
        # periodically maybe, it's not critical). Should be cached per
        # instance.number_of_products, obviously.

        context.update({
            'instance': instance,
            'products': top_products_list,
            'placeholder': placeholder,
        })
        return context
 
plugin_pool.register_plugin(TopProductsPlugin)
