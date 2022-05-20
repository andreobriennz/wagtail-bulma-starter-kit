from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import StreamField

from base.blocks import BaseStreamBlock


class ArticlePage(Page):
    subtitle = models.CharField(max_length=255, null=True, blank=True)

    description = models.CharField(max_length=255, null=True, blank=True, help_text="Used in cards which link to the article (not the article itself)")

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

    parent_page_types = ["base.ArticleIndexPage"]

    child_page_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["display_breadcrumbs"] = True
        return context

    def get_template(self, request, *args, **kwargs):
        return "pages/standard_page.html"
