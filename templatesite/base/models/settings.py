from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel


@register_setting
class ContactSettings(BaseSetting):
    email = models.EmailField(null=True)

    phone = models.CharField(null=True, max_length=50)

    address = RichTextField(null=True, features=["bold", "br"])

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
