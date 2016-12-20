from django.db.models import TextField
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailforms.models import AbstractFormField, AbstractEmailForm


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')


class FormPage(AbstractEmailForm):
    header_text = TextField()
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField()

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('header_text', classname='full'),
        FieldPanel('intro', classname='full'),
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text', classname='full'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname='col6'),
                FieldPanel('to_address', classname='col6'),
            ]),
            FieldPanel('subject'),
        ], 'Email'),
    ]

    parent_page_types = ['HomePage']
    subpage_types = []
