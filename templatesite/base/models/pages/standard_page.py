from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import StreamField

from base.blocks import BaseStreamBlock


class StandardPage(Page):
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content = StreamField(
        BaseStreamBlock(required=False),
        verbose_name="Main Content",
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle", classname="full"),
        FieldPanel("banner_image"),
        FieldPanel("content"),
    ]

    child_page_types = ["base.StandardPage"]

    def get_template(self, request, *args, **kwargs):
        return "pages/standard_page.html"
