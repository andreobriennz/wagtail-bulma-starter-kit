from django.apps import apps
from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
)
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from base.blocks import BaseStreamBlock


class StandardPage(Page):
    subtitle = models.CharField(max_length=255, null=True, blank=False)
    
    banner_image = models.ForeignKey(
        "base.CustomImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content = StreamField(
        BaseStreamBlock(required=False), verbose_name="Content", blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle", classname="full"),
        ImageChooserPanel("banner_image"),
        StreamFieldPanel("content"),
    ]

    child_page_types = ["base.StandardPage"]

    def get_template(self, request, *args, **kwargs):
        return "pages/standard_page.html"
