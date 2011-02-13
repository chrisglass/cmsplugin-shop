from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

class CartCMSPlugin(CMSPluginBase):
    model = CMSPlugin
    name = _("django SHOP Cart")
    render_template = "cmsplugin_shop/cart.html"

    def render(self, context, instance, placeholder):
        return context

plugin_pool.register_plugin(CartCMSPlugin)
