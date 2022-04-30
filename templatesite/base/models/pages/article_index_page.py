from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel,
)
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from base.models.pages import ArticlePage


class ArticleIndexPage(Page):
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    
    banner_image = models.ForeignKey(
        "base.CustomImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle", classname="full"),
        ImageChooserPanel("banner_image"),
    ]

    child_page_types = ["base.ArticlePage"]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["articles"] = ArticlePage.objects.live().public()
        return context

    def get_template(self, request, *args, **kwargs):
        return "pages/article_index_page.html"
