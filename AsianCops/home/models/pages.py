from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel, RichTextFieldPanel
from wagtail.wagtailcore.blocks import ListBlock
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from .blocks import ImageBlock, EventListBlock, PeopleBlock
from .forms import FormPage


class HomePage(Page):
    body = StreamField([
        ('image_carousel', ListBlock(ImageBlock(),
                                     template='blocks/carousel.html',
                                     icon='image')),
    ], blank=True, null=True)

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    template = 'home/default_page.html'
    parent_page_types = []
    subpage_types = [
        'EventListPage',
        'AboutUsPage',
        FormPage,
    ]


class EventListPage(Page):
    body = StreamField([
        ('event', ListBlock(EventListBlock(), template='blocks/event_list.html')),
    ], blank=True, null=True)

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    # template = 'home/default_page.html'
    parent_page_types = ['HomePage']
    subpage_types = ['EventDetailPage', 'GalleriesPage']


class EventDetailPage(Page):
    # event_title = TextField()
    long_desc = RichTextField()
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    doc = models.ForeignKey(
        'wagtaildocs.Document',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    content_panels = Page.content_panels + [
        # FieldPanel('title'),
        DocumentChooserPanel('doc'),
        ImageChooserPanel('image'),
        RichTextFieldPanel('long_desc')
        # FieldPanel('long_desc')
    ]

    parent_page_types = ['EventListPage']
    subpage_types = []


class GalleriesPage(Page):
    body = StreamField([
        ('image', ListBlock(ImageBlock(), template='blocks/galleries.html')),
    ], blank=True, null=True)

    content_panels = Page.content_panels + [StreamFieldPanel('body')]
    template = 'home/default_page.html'
    parent_page_types = ['EventListPage']
    subpage_types = []


class AboutUsPage(Page):
    about_org = RichTextField()
    exec_board = StreamField([
        ('exec_board_memeber', ListBlock(PeopleBlock(), template='blocks/members.html'))
    ], blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('about_org'),
        StreamFieldPanel('exec_board')
    ]
    parent_page_types = ['HomePage']
    subpage_types = []
