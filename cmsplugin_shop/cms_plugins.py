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
        OrderItem.objects.all().group_by('product_reference')
	context.update({
            'instance': instance,
            'products': instance.products.all(),
            'placeholder': placeholder,
        })
        return context
 
plugin_pool.register_plugin(TopProductsPlugin)
