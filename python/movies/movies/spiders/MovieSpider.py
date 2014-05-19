from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log

from movies.items import GoogleMovieResultItem


class MovieSpider(Spider):
    """
    Spider for Craigslist
    """

    name = "google-spider"
    allowed_domains = "google.com"

    start_urls = ['http://www.google.com/movies?hl=en&near=New+York,+NY&sort=1']

    def parse(self, response):
        """
        Parse the data from the spider
        """
        sel = Selector(response)
        sites = sel.css('body div#movie_results div.movie_results div.movie div.header div.desc h2')
        items = []

        #start logging
        log.msg("Begin Log", level=log.INFO)

        for site in sites:
            item = GoogleMovieResultItem()
            item['data'] = site.css('a::text').extract()
            items.append(item)

        return items
