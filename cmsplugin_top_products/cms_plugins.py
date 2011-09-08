from cmsplugin_top_products.models import TopProducts
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.template.defaultfilters import title
from django.utils.translation import ugettext_lazy as _


class TopProductsPlugin(CMSPluginBase):
    model = TopProducts
    admin_preview = False
    name = title(_('top products plugin'))
    placeholders = ('feature_home',)
    render_template = "top_products/plugins/top_products.html"
    
    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'product_count': len(instance.products.all()),
            'products': instance.products.all(),
            'placeholder': placeholder,
        })
        return context
 
plugin_pool.register_plugin(TopProductsPlugin)