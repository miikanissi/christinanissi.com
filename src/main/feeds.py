from django.contrib.syndication.views import Feed
from django.utils import timezone
from django.utils.feedgenerator import Atom1Feed

from .models import Content


class LatestFeed(Feed):
    title = "Christina Nissi's Website Feed"
    author_name = "Christina Nissi"
    link = "https://christinanissi.com/"
    description = "New content posted on Christina Nissi's website."

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

    def item_updateddate(self, item):
        return item.update_date

    def item_pubdate(self, item):
        return item.publish_date

    def item_categories(self, item):
        if item.category == 1:
            return ("Art",)
        if item.category == 2:
            return ("Writing",)
        return ("Undefined",)


class AtomFeed(LatestFeed):
    feed_type = Atom1Feed
    subtitle = LatestFeed.description
