# Create your views here.

from django.contrib.syndication.views import Feed
from q4wine.news.models import News
from django.utils.feedgenerator import Atom1Feed
import string

class RssSiteNewsFeed(Feed):
    title = "News related to q4wine development stuff and its community life."
    link = "/rss/"
    description = """Here is all news related to q4wine development stuff and its community life.\
                   If you are involved into the q4wine development process, don't forget to \
                   subscribe to our RSS feed."""

    def items(self):
        return News.objects.order_by('-date')[:10]

    def item_title(self, item):
        rss_title = str(item.date.year) + "-" + str(item.date.month) + "-" + str(item.date.day)
        rss_title += " " + item.title
        return rss_title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        url = "/#" + str(item.id)
        return url

class AtomSiteNewsFeed(RssSiteNewsFeed):
    feed_type = Atom1Feed
    subtitle = RssSiteNewsFeed.description

