from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed

from .models import Art
from .models import Writing


class LatestFeed(Feed):
    title = "Christina Nissi"
    link = "https://christinanissi.com"
    description = "New content on my website."

    def items(self):
        arts = Art.objects.filter(status=1)
        writings = Writing.objects.filter(status=1)
        query = arts.union(writings)
        query_sorted = query.order_by("created_on")
        self.item_count = query_sorted.count()
        return query_sorted

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.get_description()
        # return truncatewords(item.content, 30)

    def item_link(self, item):
        return item.get_absolute_url()


class AtomFeed(LatestFeed):
    feed_type = Atom1Feed
    subtitle = LatestFeed.description
