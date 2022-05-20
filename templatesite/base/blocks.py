from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtail_link_block.blocks import LinkBlock


MINIMAL_RICHTEXT_FEATURES = ["bold", "br"]
DEFAULT_RICHTEXT_FEATURES = ["h2", "h3", "h4", "bold", "ol", "ul", "link", "document-link", "br"]


class ButtonBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True)
    style = blocks.ChoiceBlock(
        choices=[("primary", "Primary"), ("secondary", "Secondary")],
        default="primary",
        blank=True,
    )
    link = LinkBlock()


class ButtonsBlock(blocks.StructBlock):
    items = blocks.ListBlock(
        ButtonBlock(required=False, blank=True),
        blank=True,
    )

    class Meta:
        label = "Button(s)"
        template = "blocks/buttons.html"


class HorizontalRuleBlock(blocks.StaticBlock):
    class Meta:
        label = "Horizontal Line"
        template = "blocks/horizontal_rule_block.html"


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)

    class Meta:
        label = "Image"
        template = "blocks/image_block.html"


class ImageBannerBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        required=True,
        help_text="A full width banner, so should be a large high resolution photo (use photos which are at least 1920x640px).",
    )

    class Meta:
        label = "Image Banner"
        template = "blocks/image_banner_block.html"


class CTABannerBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        required=True,
        help_text="A banner which is 50% width on desktop (use photos which are at least 960x600px).",
    )
    image_side = blocks.ChoiceBlock(choices=[
        ('left', 'Left'),
        ('right', 'Right'),
    ])
    title = blocks.CharBlock(required=False)
    text = blocks.RichTextBlock(
        template="blocks/richtext_block.html",
        features=MINIMAL_RICHTEXT_FEATURES,
        required=False
    )
    buttons = ButtonsBlock(required=False, blank=True)

    class Meta:
        label = "Call to Action"
        template = "blocks/cta_banner_block.html"


class VideoBlock(blocks.StructBlock):
    url = blocks.CharBlock(
        required=True,
        help_text="A link to a video on YouTube or Vimeo (eg https://www.youtube.com/embed/YE7VzlLtp-4).",
    )
    
    class Meta:
        label = "Video"
        template = "blocks/video_block.html"


class CardItemBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    text = blocks.CharBlock(required=False)


class CardListBlock(blocks.StructBlock):
    items = blocks.ListBlock(CardItemBlock())

    class Meta:
        label = "Card List"
        help_text = "A group of cards, each containing some text and/or an image."
        template = "blocks/card_list_block.html"


class AccordionItemBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    content = blocks.RichTextBlock(
        template="blocks/richtext_block.html",
        features=DEFAULT_RICHTEXT_FEATURES,
    )

    class Meta:
        label = "Accordion"


class AccordionListBlock(blocks.StructBlock):
    items = blocks.ListBlock(AccordionItemBlock())

    class Meta:
        template = "blocks/accordion_block.html"


class CarouselItemBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock(required=False)
    text = blocks.CharBlock(required=False)


class CarouselListBlock(blocks.StructBlock):
    items = blocks.ListBlock(CarouselItemBlock())

    class Meta:
        label = "Carousel"
        template = "blocks/slick_slider.html"


class BaseStreamBlock(blocks.StreamBlock):
    text = blocks.RichTextBlock(
        template="blocks/richtext_block.html",
        features=DEFAULT_RICHTEXT_FEATURES,
    )
    buttons_block = ButtonsBlock()
    image_block = ImageBlock()
    cta_banner_block = CTABannerBlock()
    video_block = VideoBlock()
    card_list_block = CardListBlock()
    accordion_block = AccordionListBlock()
    horizontal_rule = HorizontalRuleBlock()
    # carousel = CarouselListBlock() # uncomment only if a carousel is required
