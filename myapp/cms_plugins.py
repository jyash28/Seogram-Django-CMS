from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from myapp.models import Card, Servicecard, Pricecard,Blogcard


@plugin_pool.register_plugin
class CardPluginPublisher(CMSPluginBase):
    model = Card  # model where plugin data are saved
    module = _("myapp")
    name = _("Card Plugin")  # name of the plugin in the interface
    render_template = "card.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


@plugin_pool.register_plugin
class ServicePluginPublisher(CMSPluginBase):
    model = Servicecard
    module = _("myapp")
    name = _("service Plugin")
    render_template = "servicecard.html"


@plugin_pool.register_plugin
class PlanPluginPublisher(CMSPluginBase):
    model = Pricecard
    module = _("myapp")
    name = _("plan Plugin")
    render_template = 'pricingdata.html'


@plugin_pool.register_plugin
class BlogCardPluginPublisher(CMSPluginBase):
    model = Blogcard
    module = _("myapp")
    name = _("blog Plugin")
    render_template = 'blogdata.html'

