from glob import glob
import itertools
import os

from django import forms
from django.conf import settings

from .models import MarkdownFilePlugin


def get_mkd_choices():
    os.chdir(settings.MARKDOWN_ROOT)
    patterns = ('*.markdown', '*.mkd', )
    matches = itertools.chain.from_iterable(glob(pattern) for pattern in patterns)
    return [(x, x) for x in matches]


class MarkdownFilePluginForm(forms.ModelForm):
    class Meta:
        model = MarkdownFilePlugin

    def __init__(self, *args, **kwargs):
        super(MarkdownFilePluginForm, self).__init__(*args, **kwargs)
        self.fields['markdown_file'] = forms.ChoiceField(choices=get_mkd_choices())
