from cms.models.pluginmodel import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from shop.util.cart import get_or_create_cart

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
