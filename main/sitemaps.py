from django.contrib.sitemaps import Sitemap

from .models import Content


class ContentSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Content.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.updated_on
