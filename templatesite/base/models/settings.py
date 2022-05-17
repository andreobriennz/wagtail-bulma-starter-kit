from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel


MINIMAL_RICHTEXT_FEATURES = ["bold", "br"]


@register_setting
class SiteSettings(BaseSetting):
    seo_site_description = models.CharField(
        null=True,
        max_length=160,
        help_text="Used by search engines when there is not a specific description for the page. Should be between 50 and 160 characters (any longer and the text may be truncated by many search engines."
    )

    panels = [
        FieldPanel("seo_site_description"),
    ]


@register_setting
class ContactSettings(BaseSetting):
    email = models.EmailField(null=True)

    phone = models.CharField(null=True, max_length=50)

    address = RichTextField(null=True, features=MINIMAL_RICHTEXT_FEATURES)

    panels = [
        FieldPanel("email"),
        FieldPanel("phone"),
        FieldPanel("address"),
    ]


@register_setting
class ImageSettings(BaseSetting):
    navbar_logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    
    panels = [
        ImageChooserPanel("navbar_logo"),
    ]
