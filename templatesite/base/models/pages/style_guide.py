from wagtail.core.models import Page


class StyleGuidePage(Page):
    def get_template(self, request, *args, **kwargs):
        return "pages/style_guide.html"