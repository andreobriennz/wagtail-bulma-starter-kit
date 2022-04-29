from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


DEFAULT_RICHTEXT_FEATURES = ["h2", "h3", "h4", "bold", "ol", "ul", "link", "document-link", "br"]


class HorizontalRuleBlock(blocks.StaticBlock):
    class Meta:
        label = "Horizontal line"
        template = "blocks/horizontal_rule_block.html"


class ImageBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)

    class Meta:
        label = "Image"
        template = "blocks/image_block.html"


class ImageBannerBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)

    class Meta:
        label = "Image"
        template = "blocks/image_banner_block.html"


class VideoBlock(blocks.StructBlock):
    url = blocks.CharBlock(required=True)
    
    class Meta:
        label = "Video"
        template = "blocks/video_block.html"


class BaseStreamBlock(blocks.StreamBlock):
    text = blocks.RichTextBlock(
        template="blocks/richtext_block.html",
        features=DEFAULT_RICHTEXT_FEATURES,
    )
    image_block = ImageBlock()
    video_block = VideoBlock()
    horizontal_rule = HorizontalRuleBlock()
