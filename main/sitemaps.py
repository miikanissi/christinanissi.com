from django.contrib.sitemaps import Sitemap

from .models import Art
from .models import Writing


class WritingSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Writing.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.updated_on


class ArtSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Art.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.updated_on
