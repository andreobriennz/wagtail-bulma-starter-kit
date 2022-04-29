from django.db import models

from wagtail.images.models import Image, AbstractImage


class CustomImage(AbstractImage):
    title = models.CharField(
        max_length=255,
        verbose_name="title",
        help_text="Alternative text, essential for accessibility and SEO (should be descriptive)."
    )
