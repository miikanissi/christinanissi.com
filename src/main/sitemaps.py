from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone

from .models import Content


class ContentSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Content.objects.filter(status=1, publish_date__lt=timezone.now())

    def lastmod(self, obj):
        return obj.update_date


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return ["index", "about", "contact", "content_list", "writing_list", "art_list"]

    def location(self, item):
        return reverse(item)
