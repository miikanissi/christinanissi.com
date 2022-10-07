from django.contrib.syndication.views import Feed
from django.utils import timezone
from django.utils.feedgenerator import Atom1Feed

from .models import Content


class LatestFeed(Feed):
    title = "Christina Nissi"
    link = "https://christinanissi.com"
    description = "New content on my website."

    def items(self):
        content = Content.objects.filter(status=1, publish_date__lt=timezone.now())
        self.item_count = content.count()
        return content

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.get_description()

    def item_link(self, item):
        return item.get_absolute_url()


class AtomFeed(LatestFeed):
    feed_type = Atom1Feed
    subtitle = LatestFeed.description
