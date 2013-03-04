from django.utils.translation import ugettext_lazy as _

from django.db import models

from cms.models import CMSPlugin


class MarkdownFilePlugin(CMSPlugin):
    markdown_file = models.CharField(_("Markdown File"), max_length=255)

    def __unicode__(self):
        return self.markdown_file
