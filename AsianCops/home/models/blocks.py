from wagtail.wagtailcore.blocks import StructBlock, TextBlock, RichTextBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = TextBlock(required=False)

    class Meta:
        icon = 'image'


class EventListBlock(StructBlock):
    title = TextBlock()
    short_desc = TextBlock()
    # html_text = RawHTMLBlock(required=False)
    # image = ImageChooserBlock(required=False)
    # event_date = DateBlock()
    child_slug = TextBlock()


class PeopleBlock(StructBlock):
    name = TextBlock()
    bio = RichTextBlock()
    photo = ImageChooserBlock()
