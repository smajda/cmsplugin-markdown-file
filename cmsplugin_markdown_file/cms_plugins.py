from django.utils.translation import ugettext as _

import os
from markdown import markdown

from django.conf import settings

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import MarkdownFilePlugin
from .forms import MarkdownFilePluginForm


class CMSMarkdownFilePlugin(CMSPluginBase):
    model = MarkdownFilePlugin
    form = MarkdownFilePluginForm
    name = _('Markdown')
    render_template = 'cmsplugin_markdown_file/content.html'
    mkd_extensions = ['smartypants']
    mkd_root = getattr(settings, 'MARKDOWN_ROOT', None)

    def render(self, context, instance, placeholder):
        filename = instance.markdown_file
        if filename:
            src = os.path.join(self.mkd_root, filename)
            with open(src, 'r') as f:
                context['content'] = markdown(f.read(), extensions=self.mkd_extensions)
        return context

plugin_pool.register_plugin(CMSMarkdownFilePlugin)
