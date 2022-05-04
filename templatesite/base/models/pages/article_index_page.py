from django.db import models
from django.core.paginator import Paginator

from wagtail.admin.edit_handlers import (
    FieldPanel,
)
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from base.models.pages import ArticlePage


class ArticleIndexPage(Page):
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
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

        page = request.GET.get('page', 1)

        articles = ArticlePage.objects.live().public()

        paginated_articles = Paginator(articles, 2)

        context["paginated_articles"] = paginated_articles
        context["articles"] = list(
            paginated_articles.page(page)
        )
        context["current_page"] = page

        return context

    def get_template(self, request, *args, **kwargs):
        return "pages/article_index_page.html"
